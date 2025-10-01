from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "flax-community/t5-recipe-generation"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

special_tokens = tokenizer.all_special_tokens
tokens_map = {
    "<sep>": "--",
    "<section>": "\n"
}
def skip_special_tokens(text, special_tokens):
    for token in special_tokens:
        text = text.replace(token, "")

    return text

def target_postprocessing(texts, special_tokens):
    if not isinstance(texts, list):
        texts = [texts]
    
    new_texts = []
    for text in texts:
        text = skip_special_tokens(text, special_tokens)

        for k, v in tokens_map.items():
            text = text.replace(k, v)

        new_texts.append(text)

    return new_texts
def generate_recipe_from_ingredients(ingredients: str) -> dict:
    """
    Generate a recipe (title, ingredients, directions) from a comma-separated ingredient string.
    Returns a dict with keys: title, ingredients, instructions.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    prefix = "items: "
    input_text = prefix + ingredients
    inputs = tokenizer([input_text], max_length=256, padding="max_length", truncation=True, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    generation_kwargs = {
        "max_length": 512,
        "min_length": 64,
        "no_repeat_ngram_size": 3,
        "do_sample": True,
        "top_k": 60,
        "top_p": 0.95
    }
    with torch.no_grad():
        output_ids = model.generate(input_ids=input_ids, attention_mask=attention_mask, **generation_kwargs)
    generated= target_postprocessing(
        tokenizer.batch_decode(output_ids, skip_special_tokens=False),
        special_tokens
    )
    print(generated)
    # Post-process output to extract title, ingredients, directions
    parsed_recipe = parse_generated_recipe(generated[0])
    return parsed_recipe

def parse_generated_recipe(text: str) -> dict:
    """
    Parse the generated text into title, ingredients, and instructions.
    """
    result = {"title": "", "ingredients": "", "instructions": ""}
    lines = text.split("\n")
    section = None
    for line in lines:
        line = line.strip()
        if line.lower().startswith("title:"):
            section = "title"
            result["title"] = line[len("title:"):].strip()
        elif line.lower().startswith("ingredients:"):
            section = "ingredients"
            result["ingredients"] = line[len("ingredients:"):].strip().replace("--", "\n")
        elif line.lower().startswith("directions:"):
            section = "instructions"
            result["instructions"] = line[len("directions:"):].strip().replace("--", "\n")
        elif section and line:
            result[section] += ("\n" if result[section] else "") + line
    print(result)
    return result
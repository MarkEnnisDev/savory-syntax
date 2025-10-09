from together import Together
import json
from pydantic import BaseModel

client = Together()

## Define the schema for the output
class GeneratedRecipe(BaseModel):
    title: str
    ingredients: list[str] 
    instructions: str 
  
def generate_recipe_from_ingredients(ingredients: str) -> GeneratedRecipe:
    if ingredients == "":
      return {}
    # Generate a recipe using the ingredients passed from the form
    completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "system",
        "content": "Only respond in JSON. You are a chef assistant bot that helps users determine a recipe dependent on a comma separated list of ingredients that they input. Ensure that all ingredients that are given are present in the recipe. Ensure that the ingredient amounts are listed before each ingredient. Ensure that the instructions are in step order starting at 1 and add a newline character after each step."
      },
      {
        "role": "user",
        "content": ingredients
      },
      
    ],
    response_format={
      "type":"json_schema",
      "schema":GeneratedRecipe.model_json_schema(),
    },
    )
    # Extract the first response from the completion object to load the recipe data into the recipe
    response_content = completion.choices[0].message.content
    recipe_data = json.loads(response_content)
    recipe = GeneratedRecipe(**recipe_data)
    
    print("Completion object:", completion)
    print("Generated recipe:", json.dumps(recipe_data, indent=2))
    return recipe

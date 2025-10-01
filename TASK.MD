# TASK.md

## ✅ Completed
- [x] Initialize Django project and apps (`users`, `recipes`)
- [x] Set up SQLite3 and configure models
- [x] Create basic User model using Django auth
- [x] Build Recipe model (title, ingredients, instructions, user FK, created_at)
- [x] Implement app urls for 'core', 'recipes', and 'users' apps (2024-06-09)
- [x] Create base, home, and all required templates for 'core', 'recipes', and 'users' apps (2024-06-09)

## 🟡 In Progress 
- [] Create base HTML template and styling with TailwindCSS
- [ ] Create recipe generation view + prompt input form
- [ ] Design manual recipe creation form
- [ ] Wire frontend form to AI model and display results
- [ ] Allow user to edit generated recipes before saving
- [ ] Build Django-based AI recipe app (2024-06-09)
    - [ ] Integrate Hugging Face `flax-community/t5-recipe-generation` model via transformers
    - [ ] Build recipe generation view and prompt input form
    - [ ] Allow editing of generated recipes before saving
    - [ ] Implement manual recipe entry form
    - [ ] Implement CRUD views for recipes (list, detail, edit, delete)
    - [ ] Restrict recipe access to owner
    - [ ] Create templates: home/dashboard, recipe gen/manual form, recipe list, detail, edit, auth pages
    - [ ] Style with TailwindCSS (responsive)
    - [ ] Update README.md with setup instructions
    - [ ] (Bonus) Add search/filter, markdown/WYSIWYG, favorites, responsive improvements
    - [ ] Create and apply migrations for new models
    - [ ] Register models in Django admin
    - [ ] Scaffold forms for UserProfile and Recipe

---

## 📝 Backlog / Upcoming Tasks
- [ ] Implement user registration/login/logout with auth-protected views
- [ ] Create list/detail/edit/delete views for recipes
- [ ] User dashboard showing saved recipes
- [ ] Add search/filtering to recipe list
- [ ] Add recipe regeneration feature from saved entries
- [ ] Validate and sanitize user input before inference
- [ ] Improve UI/UX styling and responsiveness
- [ ] Write unit tests for model, forms, and views
- [ ] Create README.md with setup instructions
- [ ] Configure deployment settings for Heroku or simple VPS

---

## 🚩 Discovered Tasks (To Categorize)
- [ ] Add WYSIWYG or Markdown support to instruction input
- [ ] Add tags/categories to recipes for future sorting
- [ ] Implement pagination for recipe list

---

> 🤖 Prompt to AI Coding Assistant:
> "Update TASK.md to mark XYZ as done and add ABC as a new task."

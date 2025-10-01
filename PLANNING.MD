# PLANNING.md

## 🎯 Project Purpose & Vision
Develop a full-stack Django web application that allows users to generate and store cooking recipes using an AI model. Users can also manually enter and edit recipes. All recipes are linked to user profiles, enabling private storage and management. The core functionality blends AI generation with user control and persistence.

## 🏗️ Architecture Overview

### Backend:
- **Framework:** Django 4.x
- **Database:** SQLite3 (development) — with potential for PostgreSQL in production
- **AI Model:** `flax-community/t5-recipe-generation` via Hugging Face Transformers
- **Authentication:** Django’s built-in user model and auth system
- **App Structure:**
  - `users` – registration, login, profile
  - `recipes` – generation, manual entry, editing, storage
  - `core` – shared templates/static files and homepage

### Frontend:
- **Templating Engine:** Django Templates
- **CSS Framework:** Tailwind CSS (preferred) or Bootstrap for quick styling
- **User Interface:**
  - Responsive design
  - Recipe generation/editing form
  - User dashboard with saved recipes

## 🧱 Key Features
- AI recipe generation using ingredients

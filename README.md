AI Chatbot (React + Django)

A full-stack AI chatbot application built with React (frontend) and Django REST API (backend).
The chatbot accepts user messages and generates intelligent responses using a Large Language Model (LLM) API integration.

Features

- AI chatbot interface built with React
- Django REST API backend
- Integration with LLM API for generating responses
- Clean chat UI using Tailwind CSS and shadcn components
- API communication between frontend and backend

Tech Stack

Frontend

- React (Vite)
- Tailwind CSS
- shadcn/ui

Backend

- Django
- Django REST Framework
- Groq LLM API

Project Structure

Ai-Chatbot
 ├ backend
 │   ├ manage.py
 │   ├ uniapp
 │   └ unihelp
 │
 └ frontend
     ├ src
     ├ package.json
     └ vite.config.js

How to Run Locally

Backend

cd backend
python manage.py runserver

Frontend

cd frontend
npm install
npm run dev

Frontend runs on:

http://localhost:5173

Backend runs on:

http://127.0.0.1:8000

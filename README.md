# Gemini Terminal Chatbot

A simple command-line chatbot built with Python and Google's Gemini API. This was my first project as I learned Python by building instead of just following tutorials.

## Features
- Real-time conversation with Google's Gemini AI model
- Remembers conversation history using Gemini's chat session
- Custom personality set via a system instruction
- Graceful error handling for failed API requests

## How it works
The script uses the `google-genai` Python library to send messages to Gemini and print back responses. Conversation memory is handled by Gemini's built-in `chat` object, which resends the full conversation history with each new message.

## Setup
1. Clone this repo
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install google-genai python-dotenv`
5. Create a `.env` file with your API key:
6. Run it: `python chatbot.py`

## What I learned
- Working with external APIs
- Managing secrets safely with environment variables
- Basic error handling with try/except
- Handling chatbot conversation memory 
- Using Git and GitHub for version control
# A Medical Chatbot 

## Overview
This project implements a simple chatbot with a web-based frontend and a FastAPI backend. The chatbot responds to predefined queries related to medical topics and general conversation.

## Features
- Interactive chat interface
- Backend built using FastAPI
- Frontend built with HTML, CSS, and JavaScript
- Smooth animations and UI effects
- Asynchronous communication between frontend and backend

## Prerequisites
Ensure you have Python installed on your system. You will also need FastAPI and Uvicorn for running the backend.

Install dependencies using:
```
pip install fastapi uvicorn
```

## Project Structure
```
Chatbot-Project/
│-- frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│-- backend/
│   ├── api.py
│-- README.md
```


## Running the Project
### 1. Start the Backend
Navigate to the backend folder and run:
```
uvicorn main:app --reload
```

### 2. Open the Frontend
Simply open `index.html` in your browser.

## Conclusion
This project provides a simple chatbot with an interactive UI and a FastAPI backend. You can extend it by improving the chatbot logic, integrating a machine learning model, or deploying it online.


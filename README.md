// README.md
# Task Manager

### Introduction
Task manager is a platform that enables users manager tasks that make up 
their daily routine. A user can create a task; on creation said task is marked
as incomplete. When the task is completed, the user can mark said task as 
complete.

### Installation Guide
* Clone this repository
* The main branch is the most stable branch and at any given time, make sure you're working from it
* Run pip install -r requirements.txt to install all dependencies
* You can either work with a locally installed pg-admin or your postgresql database terminal
* Create a .env file in the root directory of the project and add the necessary environment variables

### Usage
* Run uvicorn src.main:app --reload to start the application
* Connect to the api using an api client on port 8000

### API Endpoints
| HTTP verbs | Endpoints        | Action                            |
| --- |------------------|-----------------------------------|
| POST | /api/v1/tasks/   | To create a task                  |
| GET | /api/v1/tasks/   | To fetch all tasks                |
| GET | /api/v1/tasks/1/ | To fetch a single task by id      |
|PUT | /api/v1/tasks/1/ | To update an existing task by id  |
|DELETE | /api/v1/tasks/1/ | To delete an existing task by id  |    

### Technologies Used
* Python
* Fastapi
* Postgresql

### Licence
This project is available for use under the MIT License

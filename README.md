# fastapi-project

This little project involves creating an API using FastAPI for generating random questions for a questionnaire application. 

## Installation requirements

_These packages are needed to be installed:_

sh """
pip install fastapi uvicorn
"""

## API endpoints

API Health Check

Endpoint: /testing
Method: GET
Description: Checks if the API is functioning correctly.

Endpoint: /all_questions
Method: GET
Description: Retrieves all available questions.

Endpoint: /get_questions/{use}/{subjects}/
Method: GET
Description: Retrieves random questions based on the type of test (use) and a comma-separated list of subjects (subjects). You can specify the number of questions to retrieve using the num_questions query parameter.

Endpoint: /create_question/
Method: POST
Description: Allows an admin user to create a new question. Requires authentication with admin username and password.

from fastapi import FastAPI, HTTPException, Depends, Query, Path
from typing import List
from pydantic import BaseModel

import pandas as pd
from random import sample

# add description and stuff 
api = FastAPI(
    title='QCM API'
)

# id
users = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N"
}

# basemodel to respect
class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct_answer: str
    response_A: str
    response_B: str
    response_C: str
    response_D: str

questions = []

data = pd.read_csv("questions.csv")
data = data.fillna("nothing")

for i in range(len(data)):
    q = Question(
        question = data['question'][i],
        subject = data['subject'][i],
        use = data['use'][i],
        correct_answer = data['correct'][i],
        response_A = data['responseA'][i],
        response_B = data['responseB'][i],
        response_C = data['responseC'][i],
        response_D = data['responseD'][i]
    )
    questions.append(q)
   
# just checking if api is working
@api.get('/testing')
def check_api():
    """
    checking if the API is functioning correctly
    """
    return {"message": "API is working"}

# get me all the questions
@api.get("/all_questions")
def get_all_questions():
    return questions


# random questions
@api.get('/get_questions/{use}/{subjects}/')
def get_random_questions(use: str, subjects: str = Path(...), num_questions: int = 5):
    """
    get questions randomly. it is recommended to to get 10 or 20 max. Otherwise, you will
    have a problem not having those generated questions available
    """
    subjects_list = subjects.split(",")  

    # filter questions by use and subjects
    filtered_questions = [q for q in questions if q.use == use and q.subject in subjects_list]

    # check if everything is alright
    if num_questions > len(filtered_questions):
        raise HTTPException(status_code=400, detail="Not available questions for this entry")

    # random questions
    random_questions = sample(filtered_questions, num_questions)

    return random_questions

# create new question reserved only for powerful people
@api.post('/create_question/')
def create_question(question: Question, username: str, password: str):
    """
    only admin can create questions. sorry bro!
    """
    if username != "admin" or password != users["admin"]:
        raise HTTPException(status_code=401, detail="unauthorized access!! watch out bro!")

    questions.append(question)
    return {"message": "question succesfully created"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)

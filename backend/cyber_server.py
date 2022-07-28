from fastapi import FastAPI
from typing import List
import hashlib

import database.crud as crud, database.models as models
from database.database import SessionLocal, engine
from quiz_processing.quiz_handler import prep, check
from quiz_processing.question_schema import AnsweredQuestion

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.post("/signup")
def signup(email: str, password: str):
    db = SessionLocal()

    # Replace the hashing stuff with password once the frontend is built
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    db_user = crud.get_user(db, email = email, password = hashed_password)    
    if db_user:
        db.close()
        return {"accepted": "You already have an account."}
    
    crud.create_user(db = db, email = email, password = hashed_password)
    db.close()
    
    return {"accepted": True}

@app.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    
    # Replace the hashing stuff with password once the frontend is built
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    db_user = crud.get_user(db, email = email, password = hashed_password)
    db.close()

    return {"accepted": bool(db_user)}
    
@app.post("/prep_quiz")
def prep_quiz(topic: str, difficulty: str):
    return {"quiz": prep(topic, difficulty)}

@app.post("/submit_answers")
def submit_answers(topic: str, answers: List[AnsweredQuestion]):
    results = check(topic, answers)
    return {"results": results[0], "questions_with_feedback": results[1]}

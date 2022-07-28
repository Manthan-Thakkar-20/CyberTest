from pydantic import BaseModel

class Question(BaseModel):
    number: int
    category: str
    difficulty: str
    question: str
    options: list

class AnsweredQuestion(Question):
    correct_index: int

class MarkedQuestion(AnsweredQuestion):
    feedback: str
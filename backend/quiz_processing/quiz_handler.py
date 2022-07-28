import json
import random

from .question_schema import MarkedQuestion, Question

def prep(topic, difficulty):
    try:
        quiz = json.load(open("quiz_processing/quizzes/" + topic + ".json"))
    except FileNotFoundError:
        return []
        
    questions = []

    for json_question in quiz:
        json_question.pop("correct_index")
        json_question.pop("feedback")
        questions.append(Question(**json_question))

    allowed_qs = []

    for question in questions:
        random_no = random.randint(1, 3)

        if ((question.difficulty != difficulty and random_no == 1) or (question.difficulty == difficulty and random_no != 1)):
            allowed_qs.append(questions.pop(questions.index(question)))
        
    while len(allowed_qs) < 15:
        allowed_qs.append(questions.pop(random.randint(0, len(questions) - 1)))

    random.shuffle(allowed_qs)

    while len(allowed_qs) > 15:
        allowed_qs.pop()

    return allowed_qs

def check(topic, answers):
    quiz = json.load(open("quiz_processing/quizzes/" + topic + ".json"))
    questions = []

    for json_question in quiz:
        questions.append(MarkedQuestion(**json_question))

    correct = []
    checked_questions = []

    for answer in answers:
        question = questions[answer.number - 1]
        correct.append(answer.correct_index == question.correct_index)
        checked_questions.append(question)

    return [correct, checked_questions]

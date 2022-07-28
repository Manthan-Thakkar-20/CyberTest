from fastapi.testclient import TestClient
from cyber_server import app

client = TestClient(app)

def submit_answers(answers):
    results = []

    for answer in answers:
        response = client.post(url = f"/submit_answers?topic={answer[0]}", json = answer[1]).json()

        for result in response["results"]:
            results.append(result)

    return results

def test_correct_answers():
    answers = [
                ["cyber", [ {
                                "number": 1,
                                "category": "networking",
                                "difficulty": "hard",
                                "question": "Which of the following commands will connect to host 192.168.15.1 on port 8897 and send any available output to the screen?",
                                "options": ["a", "b", "c", "d"],
                                "correct_index": 3
                            },
                            {
                                "number": 2,
                                "category": "vulnerabilites",
                                "difficulty": "easy",
                                "question": "Which of the following events should be classified as a potential incident?",
                                "options": ["a", "b", "c"],
                                "correct_index": 0
                            },
                            {
                                "number": 3,
                                "category": "networking",
                                "difficulty": "medium",
                                "question": "You are examining the results of a web browsing session. What can you derive from the following?:\nGET /sample_directory/sample_file.html HTTP/1.1 Authorization: Basic em9tYmllOmJyYWlucw==",
                                "options": ["True", "False"],
                                "correct_index": 1
                            }
                        ]
                ]
            ]

    for mark in submit_answers(answers):
        assert mark

def test_incorrect_answers():
    answers = [
                ["cyber", [ {
                                "number": 1,
                                "category": "networking",
                                "difficulty": "hard",
                                "question": "Which of the following commands will connect to host 192.168.15.1 on port 8897 and send any available output to the screen?",
                                "options": ["a", "b", "c", "d"],
                                "correct_index": 2
                            },
                            {
                                "number": 2,
                                "category": "vulnerabilites",
                                "difficulty": "easy",
                                "question": "Which of the following events should be classified as a potential incident?",
                                "options": ["a", "b", "c"],
                                "correct_index": 1
                            },
                            {
                                "number": 3,
                                "category": "networking",
                                "difficulty": "medium",
                                "question": "You are examining the results of a web browsing session. What can you derive from the following?:\nGET /sample_directory/sample_file.html HTTP/1.1 Authorization: Basic em9tYmllOmJyYWlucw==",
                                "options": ["True", "False"],
                                "correct_index": 0
                            }
                        ]
                ]
            ]

    for mark in submit_answers(answers):
        assert not mark
        
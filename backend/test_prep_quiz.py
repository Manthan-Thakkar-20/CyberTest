from fastapi.testclient import TestClient
from cyber_server import app

client = TestClient(app)

def test_prep_quiz():
    topics = ["cyber"]
    difficulties = ["easy", "medium", "hard"]

    for topic in topics:
        for difficulty in difficulties:
            result = client.post(url = f"/prep_quiz?topic={topic}&difficulty={difficulty}").json()
            assert type(result["quiz"]) == list
            assert not len(result["quiz"]) < 15
            
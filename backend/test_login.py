from fastapi.testclient import TestClient
from cyber_server import app

client = TestClient(app)

def login(valid):
    filename = "test_login_valid.csv" if valid else "test_login_invalid.csv"
    
    with open(filename, "r") as test_login:
        tests = test_login.readlines()

        cases = []

        for test in tests:
            email, password = test.split(",")
            response = client.post(url = f"/login?email={email}&password={password}").json()
            cases.append(response == {"accepted": True})
            
        return cases

def test_valid():
    cases = login(True)
    for case in cases:
        assert case

def test_invalid():
    cases = login(False)
    for case in cases:
        assert not case

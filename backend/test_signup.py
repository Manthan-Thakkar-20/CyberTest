from fastapi.testclient import TestClient
from cyber_server import app

client = TestClient(app)

# Remember to put all valid inputs into the invalid csv (since the valid input are added to the database)
def signup(valid):
    filename = "test_signup_valid.csv" if valid else "test_signup_invalid.csv"
    
    with open(filename, "r") as test_login:
        tests = test_login.readlines()

        cases = []

        for test in tests:
            email, password = test.split(",")
            response = client.post(url = f"/signup?email={email}&password={password}").json()
            cases.append(response == {"accepted": True})
            
        return cases

def test_valid():
    cases = signup(True)
    for case in cases:
        assert case

def test_invalid():
    cases = signup(False)
    for case in cases:
        assert not case

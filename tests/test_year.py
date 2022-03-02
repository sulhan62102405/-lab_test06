from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)

def test_year_get_api():
    input = "2543"
    output = 22
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age":output}



import service 
from fastapi.testclient import TestClient


client = TestClient()

def test_lenght():
    result = service.checklength("ayushtiwari@gmail.com")
    assert result ==21


def test_string():
    result  = service.check("ayushtiwari@gmail.com")
    assert result == "ayushtiwari"

def test_insert_user():
    result = service.insert_name("ayushtiwari@gmail.com")
    assert  result == "ayushtiwari@gmail.com"



def test_get_user():
    result = service.get_name("ayusht")



def test_functional_get_name():
    response = client.get("/")
    assert response.status_code == 200
    assert "shortened_names" in response.json()
    assert "lenghts" in response.json()


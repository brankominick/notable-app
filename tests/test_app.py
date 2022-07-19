from project.app import app
import json

def test_home_status_code(test_client):
    response = test_client.get('/')

    assert response.status_code == 200

def test_home_data(test_client):
    response = test_client.get('/')

    assert response.json == {"Data" : "Hello Notable"}

def test_get_docs(test_client):
    response = test_client.get('/doctors')

    assert len(response.json) == 2

def test_get_appointment_for_nadya(test_client):
    data = {'doc_id' : '1'}

    response = test_client.get('/appointments', query_string={"doc_id" : "1"})

    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_all_appointments(test_client):
    response = test_client.get('/appointments')

    assert len(response.json) == 2



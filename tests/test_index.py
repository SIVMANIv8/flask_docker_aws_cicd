from flask_docker_aws_cicd.app import app
import json

def test_index_route():
     response = app.test_client().get('/')
     assert response.status_code == 200

def test_requirement_route():
     resp = app.test_client().get('/requirements')
     assert resp.status_code == 200, "Invalid status response"
     data = json.loads(resp.data.decode('utf-8'))
     assert type(data) is dict,  "Invalid response content"
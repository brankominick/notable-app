import pytest
from project.app import app 

@pytest.fixture()
def test_client():
    return app.test_client()
from app.hello_world import greetings, code_exc
import pytest


@pytest.mark.unit
def test_hello_world():
    response = greetings("Alice")
    assert response == "Hello Alice"


@pytest.mark.unit
def test_code_exc():
    code_exc()
    assert 0
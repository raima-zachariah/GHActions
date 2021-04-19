from app.hello_world import greetings
import pytest


@pytest.mark.unit
def test_hello_world():
    response = greetings("Alice")
    assert response == "Hello Alice"
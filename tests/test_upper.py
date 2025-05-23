from app import make_uppercase

def test_make_uppercase():
    assert make_uppercase("hello") == "HELLO"
    assert make_uppercase("Hello") == "HELLO"
    assert make_uppercase("HELLO") == "HELLO"
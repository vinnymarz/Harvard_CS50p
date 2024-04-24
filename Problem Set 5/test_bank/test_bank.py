from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello, how are you today?") == 0

def test_h():
    assert value("hi") == 20
    assert value("how are you?") == 20

def test_other():
    assert value("good morning") == 100
    assert value("nice weather we are having today, isn't it?") == 100

def test_int():
     assert value("1234567890") == 100

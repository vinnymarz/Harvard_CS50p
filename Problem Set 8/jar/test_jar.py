from jar import Jar

def test_init():
    # Test case 1: Default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test case 2: Custom capacity
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    # Test case 3: Invalid capacity
    try:
        jar = Jar(-5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

    jar.deposit(6)
    assert jar.size == 8

    try:
        jar.deposit(-3)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        jar.deposit(10)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    try:
        jar.withdraw(-3)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        jar.withdraw(10)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        jar.withdraw(6)
        assert False, "Expected ValueError"
    except ValueError:
        pass

from hello import say_hello, add

def test_say_hello():
    assert (
        say_hello("Vishesh")
        == "Hello, Vishesh, welcome to Data Engineering Systems (IDS 706)!"
    )

def test_add():
    assert add(3, 5) == 8
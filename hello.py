"""IDS706 Week 1 Assignment

Contains a simple string function and a pure arithmetic function, and a
main block for manual runs. Tests can import the functions without
executing the main block.
"""
def say_hello(name: str) -> str:
    """Return a greeting message to students in the IDS class."""
    return f"Hello, {name}, welcome to Data Engineering Systems (IDS 706)!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    # Code below runs only when this file is executed directly
    print(say_hello("Pinaki"))
    print("3 + 5 =", add(3, 5))

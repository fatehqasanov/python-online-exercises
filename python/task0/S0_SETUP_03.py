def eq(actual, expected):
    """
    Minimal test helper.
    Raises AssertionError if values differ.
    """
    if actual != expected:
        raise AssertionError(f"Expected {expected!r}, got {actual!r}")

def main():
    eq(2 + 2, 4)
    print("eq() helper works")

if __name__ == "__main__":
    main()

def add(a: int, b: int) -> int:
    return a + b


def main():
    print(add(2, 3))
    print(add("a", "b"))

    # Type hints are for tooling and readability;
    # Python does not enforce them at runtime.


if __name__ == "__main__":
    main()

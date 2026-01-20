def main():
    x = 10
    print(x, type(x).__name__)

    x = 3.14
    print(x, type(x).__name__)

    x = "hello"
    print(x, type(x).__name__)

    x = [1, 2, 3]
    print(x, type(x).__name__)

    # Dynamic typing means a variable name is not bound to a single type;
    # it can reference values of different types at runtime.


if __name__ == "__main__":
    main()

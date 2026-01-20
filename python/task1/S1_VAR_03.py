def main():
    lst = [1, 2, 3]
    lst[1] = 99
    print("list after change:", lst)

    tup = (1, 2, 3)
    try:
        tup[1] = 99  # type: ignore
    except TypeError as e:
        print("tuple change error:", e)

    # Lists are mutable (you can change elements in place).
    # Tuples are immutable (their contents cannot be changed after creation).


if __name__ == "__main__":
    main()

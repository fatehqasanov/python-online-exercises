def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print("a == b:", a == b)  # same contents
    print("a is b:", a is b)  # different objects
    print("a is c:", a is c)  # same object reference

    x = None
    print("x is None:", x is None)

    # Use is for identity, == for equality.


if __name__ == "__main__":
    main()

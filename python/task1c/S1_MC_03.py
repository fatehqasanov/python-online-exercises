def calc(a, op, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


def main():
    tests = [
        (2, "+", 3),
        (10, "-", 4),
        (3, "*", 5),
        (8, "/", 2),
        (8, "/", 0),
        ("2", "+", 3),
        (1, "^", 2),
    ]

    for a, op, b in tests:
        print((a, op, b), "->", calc(a, op, b))


if __name__ == "__main__":
    main()

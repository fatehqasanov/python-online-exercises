def is_truthy(v):
    return bool(v)


def main():
    test_values = [0, 1, "", "0", [], [0], {}, None]

    for v in test_values:
        print(f"{v!r:<6} -> {is_truthy(v)}")


if __name__ == "__main__":
    main()

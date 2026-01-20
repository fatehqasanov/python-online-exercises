def normalize_name(x):
    if not x:
        return "Anonymous"

    name = x.strip()
    if not name:
        return "Anonymous"

    return name


def main():
    tests = ["", " ", None, " Ola "]

    for t in tests:
        print(f"{t!r} -> {normalize_name(t)}")


if __name__ == "__main__":
    main()

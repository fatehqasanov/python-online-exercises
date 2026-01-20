def omit(d, keys):
    return {k: v for k, v in d.items() if k not in keys}


def main():
    data = {"a": 1, "b": 2, "c": 3}
    print(omit(data, ["b"]))
    print(omit(data, ["a", "c"]))


if __name__ == "__main__":
    main()

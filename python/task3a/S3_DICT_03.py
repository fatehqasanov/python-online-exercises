def pick(d, keys):
    return {k: d[k] for k in keys if k in d}


def main():
    data = {"a": 1, "b": 2, "c": 3}
    print(pick(data, ["a", "c"]))
    print(pick(data, ["x", "a"]))


if __name__ == "__main__":
    main()

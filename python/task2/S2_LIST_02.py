def unique(values):
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result


def main():
    print(unique([1, 2, 2, 3, 1, 4, 4]))
    print(unique(["a", "b", "a", "c", "b"]))


if __name__ == "__main__":
    main()

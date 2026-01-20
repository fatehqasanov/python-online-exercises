def invert(d):
    result = {}
    for k, v in d.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result


def main():
    data = {"a": 1, "b": 2, "c": 1}
    print(invert(data))


if __name__ == "__main__":
    main()

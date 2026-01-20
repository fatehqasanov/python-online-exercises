def flatten1(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                result.append(x)
        else:
            result.append(item)
    return result


def main():
    print(flatten1([1, [2, 3], 4, [5]]))
    print(flatten1([[1, 2], [], [3], 4]))


if __name__ == "__main__":
    main()

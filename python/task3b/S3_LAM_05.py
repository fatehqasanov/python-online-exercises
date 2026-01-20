def at_least(min_value):
    return lambda x: x >= min_value


def main():
    nums = [1, 5, 10, 15]

    pred = at_least(10)
    print(list(filter(pred, nums)))


if __name__ == "__main__":
    main()

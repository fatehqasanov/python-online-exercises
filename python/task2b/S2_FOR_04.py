def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts


def main():
    print(count_occurrences(["a", "b", "a", "c", "b", "a"]))
    print(count_occurrences([1, 2, 2, 3, 3, 3]))


if __name__ == "__main__":
    main()

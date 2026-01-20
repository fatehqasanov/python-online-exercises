def sum_nested(matrix):
    total = 0

    for row in matrix:
        if not isinstance(row, list):
            return None
        for n in row:
            total += n

    return total


def main():
    print(sum_nested([[1, 2], [3, 4]]))     # 10
    print(sum_nested([[0], [-1, 1, 2]]))    # 2
    print(sum_nested([1, [2, 3]]))          # None


if __name__ == "__main__":
    main()

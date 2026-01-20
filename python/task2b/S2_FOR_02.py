def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


def main():
    print(find_first_even([1, 3, 5, 8, 10]))
    print(find_first_even([1, 3, 5]))
    print(find_first_even([]))


if __name__ == "__main__":
    main()

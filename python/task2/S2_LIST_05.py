def stats(nums):
    if not nums:
        return None

    total = 0
    mn = nums[0]
    mx = nums[0]

    for n in nums:
        total += n
        if n < mn:
            mn = n
        if n > mx:
            mx = n

    return {
        "min": mn,
        "max": mx,
        "sum": total,
        "avg": total / len(nums),
    }


def main():
    print(stats([1, 2, 3, 4]))
    print(stats([-5, 0, 5]))
    print(stats([]))


if __name__ == "__main__":
    main()

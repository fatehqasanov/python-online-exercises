def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total


def main():
    print(sum_until([1, 2, 3, 4], 5))   # 1+2=3, next 3 would exceed -> 3
    print(sum_until([5, 1, 1], 6))      # 5+1=6 -> 6
    print(sum_until([10], 9))          # 0


if __name__ == "__main__":
    main()

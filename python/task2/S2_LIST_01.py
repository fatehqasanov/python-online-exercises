def clean_numbers(values):
    result = []
    for s in values:
        try:
            result.append(float(s.strip()))
        except (ValueError, AttributeError):
            # AttributeError covers cases where s is not a string
            continue
    return result


def main():
    print(clean_numbers([" 1 ", "x", "2"]))
    print(clean_numbers(["3.5", "  4  ", "bad", "", "0"]))


if __name__ == "__main__":
    main()

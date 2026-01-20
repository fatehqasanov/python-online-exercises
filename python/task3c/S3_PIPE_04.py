def to_float(values):
    for v in values:
        try:
            yield float(v.strip())
        except Exception:
            continue


def main():
    data = [" 1 ", "x", "2", " 3 "]
    doubled = (v * 2 for v in to_float(data))
    print(sum(doubled))


if __name__ == "__main__":
    main()

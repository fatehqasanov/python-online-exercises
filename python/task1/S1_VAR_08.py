def main():
    big_int = 10 ** 100
    big_float = float(big_int)

    print("big_int type:", type(big_int).__name__)
    print("digits in big_int:", len(str(big_int)))

    print("big_float:", big_float)
    print("big_float type:", type(big_float).__name__)

    # Python integers have arbitrary precision,
    # while floats lose precision for very large numbers.


if __name__ == "__main__":
    main()

def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run


def main():
    f = compose(
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 3,
    )

    print(f(5))  # (5-3)*2+1 = 5


if __name__ == "__main__":
    main()

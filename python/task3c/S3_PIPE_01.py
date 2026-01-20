def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run


def main():
    f = pipe(
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 3,
    )

    print(f(5))  # ((5+1)*2)-3 = 9


if __name__ == "__main__":
    main()

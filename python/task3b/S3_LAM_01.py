square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"


def main():
    print(square(4), square(7))
    print(is_odd(3), is_odd(4))
    print(greet("Ola"), greet("Ada"))


if __name__ == "__main__":
    main()

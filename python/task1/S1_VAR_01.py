def main():
    values = {
        "int": 42,
        "float": 3.14,
        "str": "hello",
        "bool": True,
        "none": None,
        "list": [1, 2, 3],
        "tuple": (1, 2, 3),
        "dict": {"a": 1},
        "set": {1, 2, 3},
        "function": main,
    }

    print(f"{'name':<10} {'value':<20} {'type':<20} {'type name'}")
    print("-" * 70)

    for name, value in values.items():
        print(
            f"{name:<10} "
            f"{str(value):<20} "
            f"{str(type(value)):<20} "
            f"{type(value).__name__}"
        )


if __name__ == "__main__":
    main()

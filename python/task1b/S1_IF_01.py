def shipping_cost(weight_kg, is_member):
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None

    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost


def main():
    tests = [
        (0.5, False),
        (1, True),
        (3, False),
        (5, True),
        (10, False),
        (-1, True),
    ]

    for w, m in tests:
        print(w, m, "->", shipping_cost(w, m))


if __name__ == "__main__":
    main()

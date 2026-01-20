def group_by(items, key):
    result = {}
    for item in items:
        if key not in item:
            continue
        value = item[key]
        result.setdefault(value, []).append(item)
    return result


def main():
    users = [
        {"name": "Ola", "role": "admin"},
        {"name": "Max", "role": "user"},
        {"name": "Ada", "role": "admin"},
    ]

    print(group_by(users, "role"))


if __name__ == "__main__":
    main()

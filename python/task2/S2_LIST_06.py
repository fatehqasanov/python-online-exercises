def active_user_names(users):
    names = [u["name"].upper() for u in users if u.get("active") is True and "name" in u]
    return sorted(names)


def main():
    users = [
        {"id": 1, "name": "Ola", "active": True},
        {"id": 2, "name": "Max", "active": False},
        {"id": 3, "name": "Ada", "active": True},
        {"id": 4, "name": "Zen", "active": True},
    ]
    print(active_user_names(users))


if __name__ == "__main__":
    main()

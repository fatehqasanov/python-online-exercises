def parse(line):
    parts = line.split()
    result = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            result[k] = v
    return parts[0].rstrip(":"), result


def main():
    lines = [
        "INFO: user=42 action=login",
        "ERROR: user=10 action=fail",
        "INFO: user=7 action=logout",
    ]

    users = []
    for line in lines:
        level, data = parse(line)
        if level == "INFO" and "user" in data:
            try:
                users.append(int(data["user"]))
            except ValueError:
                pass

    print(users)


if __name__ == "__main__":
    main()

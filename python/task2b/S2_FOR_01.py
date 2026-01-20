def get_path(obj, path, fallback=None):
    current = obj
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return fallback
        current = current[part]
    return current


def main():
    data = {"a": {"b": {"c": 42}}}

    print(get_path(data, "a.b.c", None))
    print(get_path(data, "a.b.x", "N/A"))
    print(get_path(data, "a.b.c.d", "N/A"))


if __name__ == "__main__":
    main()

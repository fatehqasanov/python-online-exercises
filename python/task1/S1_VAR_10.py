def inspect(v):
    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": _is_iterable(v),
        "truthy": bool(v),
    }


def _is_iterable(v):
    try:
        iter(v)
        return True
    except TypeError:
        return False


def main():
    values = [0, 1, "", "hi", [], [1], {}, None, inspect, (1, 2)]

    for v in values:
        print(v, "->", inspect(v))


if __name__ == "__main__":
    main()

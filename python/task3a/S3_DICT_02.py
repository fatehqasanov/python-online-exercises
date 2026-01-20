def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}


def main():
    defaults = {"a": 1, "b": {"x": 10}}
    overrides = {"b": {"y": 20}}

    merged = merge_defaults(defaults, overrides)
    print(merged)

    # This is a shallow merge:
    # nested dicts are replaced, not merged.


if __name__ == "__main__":
    main()

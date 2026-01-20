def pipe_safe(*fns):
    def run(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return run


def main():
    f = pipe_safe(
        lambda x: x + 1,
        lambda x: x / 0,
        lambda x: x * 2,
    )

    print(f(5))


if __name__ == "__main__":
    main()

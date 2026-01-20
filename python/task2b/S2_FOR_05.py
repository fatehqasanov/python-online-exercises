def main():
    for r in range(1, 11):
        row = []
        for c in range(1, 11):
            row.append(str(r * c).rjust(4))
        print("".join(row))


if __name__ == "__main__":
    main()

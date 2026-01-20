import re


def normalize(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def main():
    print(normalize("  Ala   Ma   Kota  "))


if __name__ == "__main__":
    main()

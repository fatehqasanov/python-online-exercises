def main():
    people = [
        {"name": "Ola", "age": 30},
        {"name": "Ada", "age": 25},
        {"name": "Max", "age": 35},
    ]

    print("before:", people)
    sorted_people = sorted(people, key=lambda p: p["age"])
    print("after: ", sorted_people)


if __name__ == "__main__":
    main()

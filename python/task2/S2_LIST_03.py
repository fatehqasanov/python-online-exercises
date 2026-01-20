def chunk(lst, size):
    if not isinstance(size, int) or size <= 0:
        return None

    chunks = []
    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])
    return chunks


def main():
    print(chunk([1, 2, 3, 4, 5], 2))
    print(chunk([1, 2, 3, 4, 5], 3))
    print(chunk([1, 2, 3], 0))


if __name__ == "__main__":
    main()

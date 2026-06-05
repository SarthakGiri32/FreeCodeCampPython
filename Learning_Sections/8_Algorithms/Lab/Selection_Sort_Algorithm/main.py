def selection_sort(items):

    for i in range(len(items)):
        smallest = i
        for j in range(i + 1, len(items)):
            if items[smallest] > items[j]:
                smallest = j
        if smallest != i:
            items[i], items[smallest] = items[smallest], items[i]

    return items


def main():
    print(selection_sort([33, 1, 89, 2, 67, 245]))


if __name__ == "__main__":
    main()

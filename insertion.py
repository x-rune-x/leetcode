def insertion_sort(pairs: list[tuple]):
    results = []

    for i in range(len(pairs)):
        for j in range(i, 0, -1):
            if pairs[j - 1][0] > pairs[j][0]:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]

        results.append(list(pairs))

    return results


def main():
    print(insertion_sort([(3, "cat"), (3, "bird"), (2, "dog")]))


if __name__ == '__main__':
    main()

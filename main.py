import random
from random import randint


def create_random_list(length):
    random_list = list(range(length))

    for i, num in enumerate(random_list):
        new_index = randint(0, length-1)
        random_list[new_index], random_list[i] = random_list[i], random_list[new_index]

    return random_list


def bubble_sort(sort_list, highest_numbers):
    n = len(sort_list)
    for i in range(highest_numbers):
        swapped = False
        for j in range(0, n - i - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
                swapped = True

        if swapped is False:
            break

    return sort_list[-highest_numbers:]


def main():
    unsorted_list = create_random_list(100)  # could use random.shuffle()
    print(f'method sort: {unsorted_list}')

    sorted_list = bubble_sort(unsorted_list, 3)
    print(sorted_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



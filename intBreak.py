import heapq
import math
from functools import reduce


def int_break(n):
    known_prods = {1: 1}

    def break_up(num):
        if num in known_prods:
            return known_prods[num]

        known_prods[num] = 0 if num == n else num
        for i in range(math.ceil(num / 2), num):
            val = break_up(i) * break_up(num - i)
            known_prods[num] = max(known_prods[num], val)

        return known_prods[num]

    return break_up(n)


def int_break2(n):
    known_prods = {}
    result = 0

    for i in range(1, n + 1):
        if i == 1:
            known_prods[i] = 1
        else:
            highest_prod_i = 0
            for j in range(math.ceil(i / 2), i):
                prod = known_prods[j] * known_prods[(i - j)]
                if prod > highest_prod_i:
                    highest_prod_i = prod

            known_prods[i] = highest_prod_i if highest_prod_i > i else i
            result = highest_prod_i

    return result


def main():
    print(int_break(13))


if __name__ == '__main__':
    main()

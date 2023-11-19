import math


num_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }


def roman_to_int(s: str) -> int:
    result = 0

    for i in range(len(s)):
        if i < len(s) - 1 and num_dict[s[i]] < num_dict[s[i + 1]]:
            result -= num_dict[s[i]]
        else:
            result += num_dict[s[i]]

    return result


def int_to_roman(num: int) -> str:

    result = ""

    digit_letters = {
        3: ["", "M"],
        2: ["D", "C"],
        1: ["L", "X"],
        0: ["V", "I"]
    }

    for i in range(int(math.log10(num) + 1)):
        dig = num % 10

        letters = digit_letters[i]

        if dig < 4:
            result = dig * letters[1] + result
        elif dig == 4:
            result = letters[1] + letters[0] + result
        elif dig == 5:
            result = letters[0] + result
        elif 5 < dig < 9:
            result = letters[0] + (dig - 5) * letters[1] + result
        elif dig == 9:
            result = letters[1] + digit_letters[i + 1][1] + result

        num //= 10

    # for i in range(len(num_str)):
    #     digit = len(num_str) - i
    #     num = int(num_str[i])
    #
    #     if num < 4:
    #         for j in range(num):
    #             result = result + digit_letters[digit][1]
    #     elif num == 4:
    #         result = result + f"{digit_letters[digit][1]}{digit_letters[digit][0]}"
    #     elif num == 5:
    #         result = result + digit_letters[digit][0]
    #     elif 9 > num > 5:
    #         extra = ""
    #         for j in range(num - 5):
    #             extra += digit_letters[digit][1]
    #         result = result + f"{digit_letters[digit][0]}{extra}"
    #     elif num == 9:
    #         result = result + f"{digit_letters[digit][1]}{digit_letters[digit + 1][1]}"

    return result


def main():
    print("l" + "j")

    print(int_to_roman(6))


if __name__ == "__main__":
    main()

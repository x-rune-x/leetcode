def longest_common_prefix(strs: list[str]) -> str:
    max_prefix = min(strs, key=len)

    for i in range(len(max_prefix)):
        for string in strs:
            if string[i] != max_prefix[i]:
                return string[:i]

    return max_prefix


def main():
    print(longest_common_prefix(["dog", "racecar", "car"]))


if __name__ == '__main__':
    main()

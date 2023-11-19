import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def is_palindrome1(x: int) -> bool:
    palindromic = True

    num_string = str(x)
    for i in range(math.ceil(len(num_string) / 2)):
        if num_string[i] != num_string[-(i + 1)]:
            palindromic = False

    return palindromic


def is_palindrome2(x: int) -> bool:
    num_string = str(x)

    return num_string[:math.ceil(len(num_string) / 2)] == num_string[:(-math.ceil(len(num_string) / 2) - 1):-1]


def is_palindrome3(x: int) -> bool:
    if x < 0:
        return False

    temp = x
    reversed_num = 0

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x


def palindrome_linked_list(head: Optional[ListNode]) -> bool:
    if not head.next:
        return True

    # Find centre of linked list using two pointers, one of which travels at twice the speed of the other.
    # When the slow reaches the middle the faster will reach the end.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # travel through list from start and halfway points comparing the values.
    while prev:
        if head.val != prev.val:
            return False

        head = head.next
        prev = prev.next

    return True


def create_linked_list(nums):
    def link(i):
        if i == len(nums) - 1:
            return ListNode(nums[i])

        return ListNode(nums[i], link(i + 1))

    return link(0)


def main():
    test_input = [2, 1, 2, 1, 1]
    head = create_linked_list(test_input)

    print(palindrome_linked_list(head))


if __name__ == '__main__':
    main()

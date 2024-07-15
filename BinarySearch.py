from typing import Any

def binary_search(array: list[Any], target: Any) -> int:
    """
    Implements the binary search algorithm.

    :param array: a sorted array of elements
    :param target: the target element
    :return: the index of the target
    """
    low, high = 0, len(array)

    while True:
        middle: int = (high + low) // 2
        value: Any = array[middle]

        if value == target:
            return array.index(target)
        elif value > target:
            high = middle
        else:
            low = middle


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
    print(binary_search([2, 4, 6, 8, 10, 12, 14, 16, 18], 14))
    print(binary_search(["apple", "banana", "coconut", "doctor", "egg"], "banana"))
    print(binary_search([(2,4), (3,5), (5,1), (7,2), (8,9), (10,2)], (8,9)))
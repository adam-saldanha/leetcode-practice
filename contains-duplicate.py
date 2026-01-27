from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Given an integer array [nums], return [True] if any value appears
    more than once in the array, otherwise return [False].
    Examples
    >>> contains_duplicate([1, 2, 3, 3])
    True
    >>> contains_duplicate([1, 2, 3, 4])
    False
    """

    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            return True
    return False

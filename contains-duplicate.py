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

    Solution: Iterate through the list of nums. If the num is not present in
    the HashMap then we add it to the HashMap. Otherwise, we know that the
    num is a duplicate and we can return true. The list has n items. Adding
    the num to the HashMap is an O(1) operation. At most there is no
    duplicates, and we iterate through all n items. This results in O(n)
    efficiency.
    """

    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            return True
    return False

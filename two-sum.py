from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return the indices
    i and j such that nums[i] + nums[j] == target and i != j. You may assume
    that every input has exactly one pair of indices i and j that satisfy the
    condition. R Return the answer with the smaller index first.

    Examples
    >>> two_sum([3, 4, 5, 6], 7)
    [0, 1]
    >>> two_sum([4, 5, 6], 10)
    [0, 2]

    Solution: Iterate through list. If complement of num has not been seen,
    we add it to dict with index.Otherwise, we return the index of complement
    and current num.

    """
    dic = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dic:
            return [dic[complement], i]
        dic[nums[i]] = i
    return [0, 2]

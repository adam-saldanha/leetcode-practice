
def valid_anagram(self, s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if the two strings are anagrams of
    each other, otherwise return false.

    An anagram is a string that contains the exact same characters as another
    string, but the order of the characters can be different.
    Examples
    >>> valid_anagram("racecar", "carrace")
    True
    >>> valid_anagram("jar", "jam")
    False

    Solution: First we assert that strings s and t are same length.
    We map strings t and s. Then we assert if the maps are the same.
    Creating maps for s and t cost O(n + m).
    Checking the equivalence of the maps is O(n) or O(m).
    Overall efficiency is O(n + m)
    """
    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}

    for i in range(len(s)):
        if s[i] not in hash_s:
            hash_s[s[i]] = 1
        else:
            hash_s[s[i]] += 1

        if t[i] not in hash_t:
            hash_t[t[i]] = 1
        else:
            hash_t[t[i]] += 1

    for char in s:
        if char not in t:
            return False
        if hash_s[char] != hash_t[char]:
            return False
    return True

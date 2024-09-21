from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Check if the given strings are anagrams of each other

        Args:
            s (str): Input string 1
            t (str): Input string 2

        Returns:
            bool: True if the strings are anagrams of each other, False otherwise
        """

        return Counter(s) == Counter(t)

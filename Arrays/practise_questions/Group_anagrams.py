from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group anagrams together

        Args:
            strs (List[str]): List of strings

        Returns:
            List[List[str]]: List of grouped anagrams
        """
        anagrams = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())

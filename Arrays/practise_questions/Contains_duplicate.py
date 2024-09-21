from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Check if the given list contains any duplicate elements

        Args:
            nums (List[int]): List of integers

        Returns:
            bool: True if the list contains duplicate elements, False otherwise
        """

        con = Counter(nums)
        duplicate = False
        for key, value in con.items():
            if value > 1:
                duplicate = True
                break

        return duplicate

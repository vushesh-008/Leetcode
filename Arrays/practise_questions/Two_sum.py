from collections import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Find the indices of the two numbers that add up to the target

        Args:
            nums (List[int]): Input list of integers
            target (int): Target sum

        Returns:
            List[int]: List of indices of the two numbers that add up to the target
        """

        index = {}
        for i, num in enumerate(nums):
            if (target - num) in index:
                return (i, index[target - num])
            else:
                index[num] = i

from typing import List, Set

"""Problem Statment : 

    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Problem link : https://leetcode.com/problems/permutations/

"""


class Solution:
    def permutations(
        self,
        nums: List[int],
        map_: List[bool],
        output: List[List[int]],
        current_output: List[int],
    ) -> None:
        """Generate all the permutations of the given list of numbers

        Args:
            nums (List[int]): Input list of numbers
            map_ (List[bool]): Map to keep track of the numbers that are already used
            output (List[List[int]]): Final output list
            current_output (List[int]): Current output list

        Returns:
            None
        """

        if len(current_output) == len(nums):
            output.append(current_output.copy())
            return

        for i in range(len(nums)):
            if not map_[i]:
                current_output.append(nums[i])
                map_[i] = True
                self.permutations(nums, map_, output, current_output)
                current_output.pop()
                map_[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []
        map_ = [False for i in nums]
        self.permutations(nums, map_, output, [])

        return output


if __name__ == "__main__":
    obj = Solution()
    print(obj.permute([1, 2, 3]))
    print(obj.permute([0, 1]))
    print(obj.permute([1]))

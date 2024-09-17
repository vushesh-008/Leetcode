from typing import List

"""Probelem Statement:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequencyof at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations 
for the given input.

Problem link: https://leetcode.com/problems/combination-sum/
"""


class Solution:

    def pick_combinations(
        self,
        candidates: List[int],
        target: int,
        index: list,
        current_output: List[int],
        final_output: List[List[int]],
    ):
        """Pick combinations of numbers from the list such that the sum of the numbers is equal to the target

        Args:
            candidates (List[int]): input list
            target (int): target sum
            index (list): current index
            current_output (List[int]): current output list
            final_output (List[List[int]]): final output list
        """
        if index == len(candidates):
            if sum(current_output) == target:
                final_output.append(current_output.copy())
            return

        current_output.append(candidates[index])
        if sum(current_output) <= target:
            self.pick_combinations(
                candidates, target, index, current_output, final_output
            )
        current_output.pop()
        self.pick_combinations(
            candidates, target, index + 1, current_output, final_output
        )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all
        unique combinations in candidates where the candidate numbers sums to target.

        Args:
            candidates (List[int]): Input list
            target (int): Target sum

        Returns:
            List[List[int]]: List of all unique combinations
        """

        final_output = []
        self.pick_combinations(candidates, target, 0, [], final_output)

        return final_output


if __name__ == "__main__":

    sol = Solution()
    print(sol.combinationSum2([2, 3, 6, 7], 7))

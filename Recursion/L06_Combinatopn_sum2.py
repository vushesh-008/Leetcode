from typing import List, Set

"""Problem Statement:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates
where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Problem link: https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:

    def pick_combinations_optimized(
        self,
        candidates: List[int],
        target: int,
        index: list,
        current_output: List[int],
        final_output: List[List[int]],
        current_sum: int,
    ) -> None:
        """Pick combinations of numbers from the list such that the sum of the numbers is equal to the target

            Time complexity: O(2^n)

        Args:
            candidates (List[int]): Input list
            target (int): Target sum
            index (list): Index of the current element
            current_output (List[int]): Current output list
            final_output (Set[List[int]]): Final output list
            current_sum (int): Current sum of the elements in the output list

        Returns:
            None
        """

        if current_sum == target:
            final_output.append(current_output.copy())
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue  # Skip duplicates
            if current_sum + candidates[i] > target:
                break

            current_output.append(candidates[i])
            self.pick_combinations_optimized(
                candidates,
                target,
                i + 1,
                current_output,
                final_output,
                current_sum + candidates[i],
            )
            current_output.pop()

    def pick_combinations(
        self,
        candidates: List[int],
        target: int,
        index: list,
        current_output: List[int],
        final_output: Set[List[int]],
        current_sum: int,
    ) -> None:
        """Pick combinations of numbers from the list such that the sum of the numbers is equal to the target

            Time complexity: O(2^n)

        Args:
            candidates (List[int]): input list
            target (int): target sum
            index (list): current index
            current_output (List[int]): current output list
            final_output (List[List[int]]): final output list

        Returns:
            None
        """

        if current_sum == target:
            final_output.add(tuple(current_output.copy()))
            return
        if current_sum > target or index == len(candidates):
            return

        current_output.append(candidates[index])
        if sum(current_output) <= target:
            self.pick_combinations(
                candidates,
                target,
                index + 1,
                current_output,
                final_output,
                current_sum + candidates[index],
            )
        current_output.pop()
        self.pick_combinations(
            candidates, target, index + 1, current_output, final_output, current_sum
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
        candidates.sort()
        # self.pick_combinations(candidates, target, 0, [], final_output, 0)
        self.pick_combinations_optimized(candidates, target, 0, [], final_output, 0)

        return final_output


if __name__ == "__main__":

    sol = Solution()
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

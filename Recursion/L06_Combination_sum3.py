from typing import List

"""Probelem Statement:

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, 
    and the combinations may be returned in any order.

Problem link: https://leetcode.com/problems/combination-sum-iii/

"""


class Solution:

    def all_combinations(
        self,
        candidates: list[int],
        k: int,
        n: int,
        output: List[List[int]],
        current_sum: int,
        current_list: List[int],
        index: int,
    ):
        """Generate all combinations of numbers from the list such that the sum of the numbers is equal to the target

        Args:
            candidates (List[int]): input list
            k (int): number of elements in the combination
            n (int): target sum
            output (List[List[int]]): final output list
            current_sum (int): current sum
            current_list (List[int]): current output list
            index (int): current index

        Returns:
            None

        """
        if current_sum == n and len(current_list) == k:
            output.append(current_list.copy())
            return

        if current_sum > n or index == len(candidates) or len(current_list) >= k:
            return

        current_list.append(candidates[index])
        self.all_combinations(
            candidates,
            k,
            n,
            output,
            current_sum + candidates[index],
            current_list,
            index + 1,
        )
        current_list.pop()
        self.all_combinations(
            candidates, k, n, output, current_sum, current_list, index + 1
        )

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        candidates = [i for i in range(1, 10)]
        output = []
        self.all_combinations(candidates, k, n, output, 0, [], 0)

        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum3(3, 7))  # [[1,2,4]]
    print(sol.combinationSum3(9, 45))  # [[1,2,3,4,5,6,7,8,9]]

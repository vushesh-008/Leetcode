from typing import List


class Solution:
    def __init__(self, output: List[List[int]] = []) -> None:
        """Constructor to initialize the output list

        Args:
            output (List[List[int]], optional): _description_. Defaults to [].
        """
        self.output = output

    def pick_combinations(
        self, candidates: List[int], target: int, index: list, current_output: List[int]
    ):
        """Pick combinations of numbers from the list such that the sum of the numbers is equal to the target

        Args:
            candidates (List[int]): input list
            target (int): target sum
            index (list): current index
            current_output (List[int]): current output list
        """
        if index == len(candidates):
            if sum(current_output) == target:
                self.output.append(current_output.copy())
                print(current_output)
            return

        current_output.append(candidates[index])
        if sum(current_output) <= target:
            self.pick_combinations(candidates, target, index, current_output)
        current_output.pop()
        self.pick_combinations(candidates, target, index + 1, current_output)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.pick_combinations(candidates, target, 0, [])

        return self.output


if __name__ == "__main__":

    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))

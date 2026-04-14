from typing import List
class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_output = []
        self.pick_combinations(candidates,target,0,[],final_output)

        return final_output

    def pick_combinations(self, candidates: List[int],target: int,index:int,current_output : List[int],final_output : List[List[int]]):

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
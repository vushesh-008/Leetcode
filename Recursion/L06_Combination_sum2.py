from typing import List

"""Problem Statement:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates
where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Problem link: https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:

    def pick_combinations_set(self, candidates: List[int], target: int, index: int, 
                         current_output: List[int], final_output: set) -> None:
        """Non-optimized approach using set to eliminate duplicates.
        
        Args:
            candidates (List[int]): Sorted input list
            target (int): Target sum
            index (int): Current index
            current_output (List[int]): Current combination
            final_output (set): Set of tuples (to avoid duplicates)
        """
        if index == len(candidates):
            if sum(current_output) == target:
                final_output.add(tuple(current_output))
            return

        # Pick current element (each element used only once, so move to index+1)
        current_output.append(candidates[index])
        if sum(current_output) <= target:
            self.pick_combinations_set(candidates, target, index+1, current_output, final_output)
        current_output.pop()
        
        # Not pick current element
        self.pick_combinations_set(candidates, target, index+1, current_output, final_output)

    def pick_combinations_optimized(self, candidates: List[int], target: int, index: int, 
                         current_output: List[int], final_output: List[List[int]]) -> None:
        """Optimized solution using for-loop approach with duplicate skipping.
        
        Args:
            candidates (List[int]): Sorted input list
            target (int): Target sum
            index (int): Starting index for this recursion level
            current_output (List[int]]: Current combination
            final_output (List[List[int]]): Final output list
        """
        # Base case: found valid combination
        if sum(current_output) == target:
            final_output.append(current_output.copy())
            return 
        
        # Early pruning (optional but improves performance)
        if sum(current_output) > target:
            return
        
        # Try each candidate starting from index
        for i in range(index, len(candidates)):
            # Skip duplicates at same recursion level
            # IMPORTANT: Check i > index FIRST to avoid accessing candidates[i-1] incorrectly
            if i > index and candidates[i] == candidates[i-1]:
                continue
            
            # Pruning: if adding this element exceeds target, stop (array is sorted)
            if sum(current_output) + candidates[i] > target:
                break
                
            current_output.append(candidates[i])
            # Move to next index (each element used only once)
            self.pick_combinations_optimized(candidates, target, i+1, current_output, final_output)
            current_output.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Find all unique combinations where numbers sum to target. Each number used once.
        
        Args:
            candidates (List[int]): Input list (may contain duplicates)
            target (int): Target sum
            
        Returns:
            List[List[int]]: All unique combinations
        """
        candidates.sort()  # MUST sort for duplicate handling
        final_output = []
        
        # Use optimized approach (recommended)
        self.pick_combinations_optimized(candidates, target, 0, [], final_output)
        return final_output
        
        # Or use non-optimized with set (less efficient but simpler)
        # final_output_set = set()
        # self.pick_combinations_set(candidates, target, 0, [], final_output_set)
        # return [list(combo) for combo in final_output_set]


if __name__ == "__main__":

    sol = Solution()
    print("Example 1:", sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # Expected: [[1,1,6], [1,2,5], [1,7], [2,6]]
    
    print("Example 2:", sol.combinationSum2([2, 5, 2, 1, 2], 5))
    # Expected: [[1,2,2], [5]]
    
    print("Example 3:", sol.combinationSum2([1, 1, 1, 1], 2))
    # Expected: [[1,1]]

    print("Example 3:", sol.combinationSum2_optimized([2, 3, 6, 7], 7))

    print("Example 4:", sol.combinationSum2_optimized([2, 3, 5], 8))

    print("Example 5:", sol.combinationSum2_optimized([1,1,1,1,1,1,1,1,1,1], 4))

    print("With duplicates:", sol.combinationSum2_optimized([10, 1, 2, 7, 6, 1, 5], 8))

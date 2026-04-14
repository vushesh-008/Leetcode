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


# ============================================================================
# APPROACH 2: Using SWAP (No extra space for map_ array)
# ============================================================================
class SolutionSwap:
    """
    Space Optimized: O(1) extra space (excluding recursion stack)
    
    KEY IDEA: Instead of using a map_ array to track used elements,
              we swap elements in-place to fix positions.
    
    Algorithm:
    1. Fix position 'index' by trying every element from index to end
    2. Swap element at position 'i' to position 'index' (fixing it)
    3. Recurse for remaining positions (index+1 onwards)
    4. Backtrack by swapping back
    """
    
    def permutationsSwap(self, nums: List[int], index: int, output: List[List[int]]) -> None:
        """Generate permutations using swap approach
        
        Args:
            nums: The array being modified in-place
            index: Current position we're fixing
            output: Final output list
        """
        # Base case: all positions fixed, add current permutation
        if index == len(nums):
            output.append(nums[:])  # Add a copy of nums
            return
        
        # Try fixing each element from index to end at position 'index'
        for i in range(index, len(nums)):
            # Swap: Fix nums[i] at position 'index'
            nums[index], nums[i] = nums[i], nums[index]
            
            # Recurse: Permute remaining positions
            self.permutationsSwap(nums, index + 1, output)
            
            # Backtrack: Undo the swap
            nums[index], nums[i] = nums[i], nums[index]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.permutationsSwap(nums, 0, output)
        return output


if __name__ == "__main__":
    print("="*70)
    print("APPROACH 1: Using map_ array (O(n) extra space)")
    print("="*70)
    obj = Solution()
    print(f"permute([1, 2, 3]) = {obj.permute([1, 2, 3])}")
    print(f"permute([0, 1]) = {obj.permute([0, 1])}")
    print(f"permute([1]) = {obj.permute([1])}")
    
    print("\n" + "="*70)
    print("APPROACH 2: Using SWAP (O(1) extra space)")
    print("="*70)
    obj_swap = SolutionSwap()
    print(f"permute([1, 2, 3]) = {obj_swap.permute([1, 2, 3])}")
    print(f"permute([0, 1]) = {obj_swap.permute([0, 1])}")
    print(f"permute([1]) = {obj_swap.permute([1])}")
    
    print("\n" + "="*70)
    print("VISUALIZATION: How SWAP works for [1,2,3]")
    print("="*70)
    print("""
    Start with nums = [1, 2, 3], index = 0
    │
    ├─ Swap(0,0): [1, 2, 3] → Fix 1 at position 0
    │  ├─ Swap(1,1): [1, 2, 3] → Fix 2 at position 1
    │  │  └─ Swap(2,2): [1, 2, 3] → Fix 3 at position 2 ✓ [1,2,3]
    │  ├─ Swap(1,2): [1, 3, 2] → Fix 3 at position 1
    │  │  └─ Swap(2,2): [1, 3, 2] → Fix 2 at position 2 ✓ [1,3,2]
    │
    ├─ Swap(0,1): [2, 1, 3] → Fix 2 at position 0
    │  ├─ Swap(1,1): [2, 1, 3] → Fix 1 at position 1
    │  │  └─ Swap(2,2): [2, 1, 3] → Fix 3 at position 2 ✓ [2,1,3]
    │  ├─ Swap(1,2): [2, 3, 1] → Fix 3 at position 1
    │  │  └─ Swap(2,2): [2, 3, 1] → Fix 1 at position 2 ✓ [2,3,1]
    │
    └─ Swap(0,2): [3, 2, 1] → Fix 3 at position 0
       ├─ Swap(1,1): [3, 2, 1] → Fix 2 at position 1
       │  └─ Swap(2,2): [3, 2, 1] → Fix 1 at position 2 ✓ [3,2,1]
       └─ Swap(1,2): [3, 1, 2] → Fix 1 at position 1
          └─ Swap(2,2): [3, 1, 2] → Fix 2 at position 2 ✓ [3,1,2]
    
    Note: After each recursion returns, we swap back (backtrack)
    """)

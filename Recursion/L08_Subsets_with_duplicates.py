"""
Subsets II (Subsets with Duplicates)

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

from typing import List

class Solution:
    def pick(self, nums: List[int], index: int, current_output: List[int], final_output: set) -> None:
        """
        Recursive function to generate all subsets
        """
        if index == len(nums):
            final_output.add(tuple(current_output))
            return

        # Include the current element
        current_output.append(nums[index])
        self.pick(nums, index+1, current_output, final_output)
        current_output.pop()
        
        # Exclude the current element
        self.pick(nums, index+1, current_output, final_output)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Main function to generate all unique subsets
        """
        final_output = set()
        nums.sort()  # Sort to help with duplicate detection
        self.pick(nums, 0, [], final_output)  # ← Fixed: changed 'index' to 0
        
        return [list(combo) for combo in final_output]


# Alternative: More efficient approach without using set
class SolutionOptimized:
    def pick(self, nums: List[int], index: int, current_output: List[int], final_output: List[List[int]]) -> None:
        """
        Recursive function with skip duplicates optimization
        
        KEY INSIGHT: Add the current subset FIRST, then explore further options.
        This is different from the pick/not-pick approach where you add only at the end.
        """
        # ← MUST add current subset BEFORE the for loop, not when index == len(nums)
        final_output.append(current_output[:])  
        
        for i in range(index, len(nums)):
            # Skip duplicates: if current element is same as previous, skip it
            # This works because array is sorted
            if i > index and nums[i] == nums[i-1]:
                continue
            
            current_output.append(nums[i])
            self.pick(nums, i+1, current_output, final_output)
            current_output.pop()
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        More efficient approach - avoids using set
        """
        final_output = []
        nums.sort()
        self.pick(nums, 0, [], final_output)
        return final_output


# WRONG APPROACH - for comparison
class SolutionBuggy:
    """
    This shows the BUGGY version of your code.
    
    THE PROBLEM: You're checking if index == len(nums) and only then appending.
    But with the for-loop approach, this doesn't work correctly!
    
    Why? Because you add current subset BEFORE exploring more elements.
    When you use the for-loop pattern, you should append BEFORE the loop,
    not when you reach the end.
    """
    def pick(self, nums: List[int], index: int, current_output: List[int], final_output: List[int]) -> None:
        # ❌ WRONG: This adds subsets only when we've exhausted all elements
        # But with for-loop pattern, many valid subsets are never added!
        if index == len(nums):
            final_output.append(current_output.copy())
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue

            current_output.append(nums[i])
            self.pick(nums, i+1, current_output, final_output)
            current_output.pop()
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final_output = []
        nums.sort()
        self.pick(nums, 0, [], final_output)
        return final_output


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_opt = SolutionOptimized()
    sol_buggy = SolutionBuggy()
    
    print("="*60)
    print("COMPARING: Correct vs Buggy Implementation")
    print("="*60)
    
    # Test case 1
    nums1 = [1, 2, 2]
    result1 = sol.subsetsWithDup(nums1)
    result1_opt = sol_opt.subsetsWithDup(nums1)
    result1_buggy = sol_buggy.subsetsWithDup(nums1)
    print(f"\nTest Case 1: {nums1}")
    print(f"Expected: [[],[1],[1,2],[1,2,2],[2],[2,2]] (6 subsets)")
    print(f"✓ Correct (with set):     {sorted(result1)} ({len(result1)} subsets)")
    print(f"✓ Correct (without set):  {sorted(result1_opt)} ({len(result1_opt)} subsets)")
    print(f"✗ Buggy (your version):   {sorted(result1_buggy)} ({len(result1_buggy)} subsets) ← WRONG!")
    
    # Test case 2
    nums2 = [0]
    result2 = sol.subsetsWithDup(nums2)
    result2_opt = sol_opt.subsetsWithDup(nums2)
    result2_buggy = sol_buggy.subsetsWithDup(nums2)
    print(f"\nTest Case 2: {nums2}")
    print(f"Expected: [[],[0]] (2 subsets)")
    print(f"✓ Correct (with set):     {sorted(result2)} ({len(result2)} subsets)")
    print(f"✓ Correct (without set):  {sorted(result2_opt)} ({len(result2_opt)} subsets)")
    print(f"✗ Buggy (your version):   {sorted(result2_buggy)} ({len(result2_buggy)} subsets)")
    
    # Test case 3
    nums3 = [4, 4, 4, 1, 4]
    result3 = sol.subsetsWithDup(nums3)
    result3_opt = sol_opt.subsetsWithDup(nums3)
    result3_buggy = sol_buggy.subsetsWithDup(nums3)
    print(f"\nTest Case 3: {nums3}")
    print(f"✓ Correct (with set):     {sorted(result3)} ({len(result3)} subsets)")
    print(f"✓ Correct (without set):  {sorted(result3_opt)} ({len(result3_opt)} subsets)")
    print(f"✗ Buggy (your version):   {sorted(result3_buggy)} ({len(result3_buggy)} subsets)")
    
    print("\n" + "="*60)
    print("KEY TAKEAWAY:")
    print("="*60)
    print("With the for-loop pattern, append current subset BEFORE the loop,")
    print("not when index == len(nums)!")
    print("="*60)

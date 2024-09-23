from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Find all unique triplets in the array which gives the sum of zero

            Time complexity: O(n^2)
            Space complexity: O(n)

        Args:
            nums (List[int]): List of integers

        Returns:
            List[List[int]]: List of unique triplets
        """

        nums.sort()
        ans = []

        for i in range(len(nums)):
            # Skip the duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early termination
            if nums[i] > 0:
                break
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip the duplicates , Ex : [-1, -1, 2]
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip the duplicates , Ex : [-1, 2, 2]
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return ans


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    s = Solution()
    print(s.threeSum(nums))

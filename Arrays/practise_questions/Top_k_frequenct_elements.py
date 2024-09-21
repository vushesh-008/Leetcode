from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Extract the top k frequent elements from the given list of integers

            Time complexity: O(nlogn)
            Space complexity: O(n)

        Args:
            nums (List[int]): Input list of integers
            k (int): Number of top frequent elements to extract

        Returns:
            List[int]: List of top k frequent elements
        """

        frequency = list(Counter(nums).items())
        frequency.sort(key=lambda x: x[1], reverse=True)

        return [t[0] for t in frequency[:k]]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """Find the top k frequent elements in the list

        Args:
            nums (List[int]): Input list of integers
            k (int): Number of top frequent elements to extract

        Returns:
            List[int]: List of top k frequent elements
        """
        # Count the frequency of each element
        frequency = Counter(nums)

        # Use a heap to keep track of the top k elements
        heap = []
        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the elements from the heap
        return [heapq.heappop(heap)[1] for _ in range(len(heap))][::-1]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    s = Solution()
    print(s.topKFrequent2(nums, k))

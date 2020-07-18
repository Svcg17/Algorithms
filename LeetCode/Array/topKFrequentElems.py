"""
Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Must be of time complexity greater than nlogn
"""
from typing import List
import heapq


class Solution:
    """Solution class for Top K Frequent Elements"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Finds the kth most frequent numbers of a list
        Args:
            nums: List of integers
            k: integer representing the number of frequent numbers
            to search for
        Returns:
            the kth most frequent numbers of nums in a list
        """
        freq = {}
        heap = []

        # create dict of # of frequency
        for i in nums:
            if freq.get(i):
                freq[i] += 1
            else:
                freq[i] = 1

        for key, val in freq.items():
            # push (frequency, key) to heap every time
            heapq.heappush(heap, (val, key))
            # once length of heap surpasses k, pop the least frequent node
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]


# main
sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))
print(sol.topKFrequent([2, 2], 1))
print(sol.topKFrequent([], 0))

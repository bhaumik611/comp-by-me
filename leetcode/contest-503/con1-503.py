'''ou are given a sorted integer array nums and an integer k.

Return an array such that each distinct element appears at most k times, while preserving the relative order of the elements in nums.

Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,1,2,2,3]

Explanation:

Each element can appear at most 2 times.

The element 1 appears 3 times, so only 2 occurrences are kept.
The element 2 appears 2 times, so both occurrences are kept.
The element 3 appears 1 time, so it is kept.
Thus, the resulting array is [1, 1, 2, 2, 3].

Example 2:

Input: nums = [1,2,3], k = 1

Output: [1,2,3]

Explanation:

All elements are distinct and already appear at most once, so the array remains unchanged.

Note: Please do not copy the description during the contest to maintain the integrity of your submissions.'''

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = {}
        result = []
        
        for num in nums:
            if count.get(num, 0) < k:
                result.append(num)
                count[num] = count.get(num, 0) + 1
        
        return result
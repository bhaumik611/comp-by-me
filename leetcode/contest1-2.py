'''You are given an integer array ​​​​​​​nums.

Define a frequency balance subarray as follows:

If the subarray contains only one distinct value, it is frequency balanced.
Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.
Return an integer denoting the length of the longest frequency balance subarray.

'''

class Solution:
    def longestFrequencyBalance(self, nums: List[int]) -> int:
        from collections import Counter
        
        count = Counter()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while True:
                freq_count = Counter(count.values())
                if len(freq_count) == 1 or (len(freq_count) == 2 and sorted(freq_count.keys()) == [f, 2 * f] for f in freq_count):
                    max_length = max(max_length, right - left + 1)
                    break
                else:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
        
        return max_length
    
#final corrected code
class Solution:
    def longestFrequencyBalance(self, nums: List[int]) -> int:
        from collections import Counter
        
#test case that fails is [1,2,2,1,2,3,3,3]

        count = Counter()
        left = 0
        max_length = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while True:
                freq_count = Counter(count.values())
                if len(freq_count) == 1 or (len(freq_count) == 2 and sorted(freq_count.keys()) == [f, 2 * f] for f in freq_count):
                    max_length = max(max_length, right - left + 1)
                    break
                else:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
        return max_length
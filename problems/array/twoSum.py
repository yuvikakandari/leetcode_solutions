"""
Problem: Two Sum
Platform: LeetCode #1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Quick local test (won't run on LeetCode, LeetCode handles input automatically)
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))   # -> [0,1]
    print(s.twoSum([3,2,4], 6))       # -> [1,2]
    print(s.twoSum([3,3], 6))         # -> [0,1]

"""
Problem: 3Sum
Platform: LeetCode #15
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/
Time: O(n^2)
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for a in range(0, n - 2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            left = a + 1
            right = n - 1
            while left < right:
                total = nums[a] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[a], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# Quick local test 
if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))   # -> [[-1,-1,2], [-1,0,1]]
    print(s.threeSum([0,0,0,0]))          # -> [[0,0,0]]
    print(s.threeSum([]))                 # -> []

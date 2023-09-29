class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = list()

        for i , val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1

            while left < right:
                thrsum = val + nums[left] + nums[right]
                if thrsum < 0:
                    left += 1
                elif thrsum > 0:
                    right -= 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans


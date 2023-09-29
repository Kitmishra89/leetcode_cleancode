class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left, result, sum_target = 0, sys.maxsize, 0
        
        for i in range(0, len(nums)):
            sum_target += nums[i]
            while(sum_target>=target):
                result = min(result,(i+1-left))
                sum_target -= nums[left]
                left += 1
                
        return result if(result!=sys.maxsize) else 0
                
            
                
            
            
        
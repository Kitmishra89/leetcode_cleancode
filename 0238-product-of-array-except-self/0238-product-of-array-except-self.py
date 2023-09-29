class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix, suffix = [1]*size, [1]*size
        
        for i in range(1, size):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)
        
        for j in range(size-1, 0, -1):
            suffix[j-1] = suffix[j] * nums[j]  
            
        print(suffix)
            
        Ans = [1]*size
        for i in range(0,size):
            Ans[i] = prefix[i]*suffix[i]
            
        return Ans
        
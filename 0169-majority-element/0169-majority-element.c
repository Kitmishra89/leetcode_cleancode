int majorityElement(int* nums, int numsSize){
    
    int i, count = 1, major = nums[0];
    for(i = 1; i < numsSize; i++)
    {
        if(count == 0)
        {
            count = 1;
            major = nums[i];
        }
        
        else if(nums[i] == major)
        {
            count++;
        }
        
        else{
            count--;
        }
    }
    
return major;
}


bool canJump(int* nums, int numsSize){ 
    
    int k = 0, i=0;
    while(i<numsSize-1)
    {
        if((k-nums[i]<=1) && nums[i]==0)
        {
            return 0;
        }
        
        else if(k-nums[i]>0)
        {
            i++;
            k--;
        }
        
        else if((k-nums[i]<=0) && nums[i]>0)
        {
            k = nums[i];
            i++;
        }
    }
    
return 1;
}



























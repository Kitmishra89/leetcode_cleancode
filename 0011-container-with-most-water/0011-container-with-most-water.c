

int maxArea(int* height, int heightSize){
    
    int l=0,r=heightSize-1, max=0,new_max;
    
    while(l<r)
    {
        if(height[r]>height[l]){
            new_max = height[l]*(r-l);
            l++;
        }
        else{
            new_max = height[r]*(r-l);
            r--;
        }
        
        if(max<new_max)
                max = new_max;
    }
    
return max;    
}
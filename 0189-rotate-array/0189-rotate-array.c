

void rotate(int* nums, int numsSize, int k){
    int i,j,n=numsSize;
    int ar[n];
    if(k>n){
        k=k%n;
    }
    if(n>1){
    for(i=0;i<n;i++){
        if(i<k){
        ar[k-i-1]=nums[n-i-1];
    }
        else{
            ar[i]=nums[i-k];
        }
   }

    for(i=0;i<n;i++){
        nums[i]=ar[i];
    }
}
}
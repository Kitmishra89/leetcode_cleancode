int max(int a, int b)
{
    if(a>b)
        return a;
return b;
}

int candy(int* ratings, int ratingsSize){
    int arr[ratingsSize];
    
    int i, candy = 0;
    
    for(i=0; i<ratingsSize; i++)
    {
        arr[i] = 1;
    }
    
    for(i = 0; i<ratingsSize-1; i++)
    {
        if(ratings[i]<ratings[i+1])
        {
            arr[i+1] = arr[i] + 1;
        }
    }
    
    for(i = ratingsSize-1; i>0; i--)
    {
        if(ratings[i-1]>ratings[i])
        {
            arr[i-1] = max(arr[i-1], arr[i]+1);
        }
    }
    
    for(i = 0; i <ratingsSize; i++)
    {
        candy = candy + arr[i];
    }
    
return candy;
}


bool isHappy(int n){
    int p=n;
    if(p==1){
        return true;
    }
    while(p>0){
        int sum=0;
         if(p<6)  return false;
        else
            while(p>0){
                sum=sum+(p%10)*(p%10);
                p=p/10;
            }
        if(sum==1)  return true;
        else p=sum;
    }
     
return false;
}
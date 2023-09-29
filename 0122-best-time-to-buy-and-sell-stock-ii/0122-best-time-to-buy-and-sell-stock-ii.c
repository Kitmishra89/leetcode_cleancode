

int maxProfit(int* prices, int pricesSize){
    
    int price,sell,profit=0;
    int i=0;
    price = prices[0];
    while(i<pricesSize)
    {
        if(prices[i]>price)
        {
            profit += (prices[i]-price); 
            price = prices[i];
            i++;
            printf("%d ",profit);
        }
        
        else if(prices[i]<price)
        {
            price = prices[i];
            i++;
        }
        else{
            i++;
        }
    }
return profit;
}
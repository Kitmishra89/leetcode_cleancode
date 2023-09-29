

int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize){
    
    int totalgas = 0, totalcost = 0, max = 0, i, index = 0;
    for(i=0; i<gasSize;)
    {
        if((gas[i] + max) >= cost[i]){
            max = max + gas[i] - cost[i];
            totalgas += gas[i];
            totalcost += cost[i];
            i++;
        }
        
        else{
            totalgas += gas[i];
            totalcost += cost[i];
            i++;
            index = i;
            max = 0;
        }
        
    }
    
  //  printf("%d %d",totalgas,totalcost);
    
    if(totalgas>=totalcost)
        return index;

return -1;
}
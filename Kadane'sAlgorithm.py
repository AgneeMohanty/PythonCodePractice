#Given an array arr of length n , consisting of integewrs.  find the sum of the subarray(including empty subarray) having  maximum sum among all subarrays.
#The array includes negative numbers as well.
#Lets solve this problem using a hash set where we can add all possible subarrays
#as the keys and their sum as their values.
#These possible combinations can be found if we keep appending next next
#Then we can choose the subarray with max sum
def Kadanesalgo(num:list[int])->list[int]:
    n=len(num)
    numdict={}
    for i in range(n):
        for j in range(i+1,n):
            numdict[tuple(num[i:j+1])]=None# this was needed because we cant add mutable(objects) as keys.
    #Now to populate the dictionary values with sum
    for i in numdict:
        sum1=0
        for j in i:
            sum1+=j
        numdict[i]=sum1
        
    print(numdict)
    min_value = float('-inf')
    j=0
    #Now to find the key with max value,
    for i in numdict:
        if numdict[i]>min_value:
            min_value=numdict[i]#will determine the sum
            
    return min_value
print(Kadanesalgo([1, 2, 7, -4, 3, 2, -10, 9, 1]))

            

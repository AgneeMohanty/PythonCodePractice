#Given a array containing prices of stock from day 1 onwards,find the day on which to buy and sell the stock for maximum profit.
#We have to keep in mind, not any pair will work, because we can sell a stock on higher price that comes after it not before it
#for example in array 5,3,4,1,2 ...(5,3) pair is not possible as 5 was a older price
def buyandsellStock(nums:list[int])->list[int]:
    n=len(nums)
    lst=[]
    count =0
    res=[]
   # maxcount=0
    for i in range(n):
        for j in range(i+1,n):
    
                lst.append((nums[i],nums[j]))
    print(lst)
    for i in lst:
          if (i[1]-i[0]) >count:
            count=i[1]-i[0]
            sell=i[1]
            buy=i[0]
    return [buy,sell]
    
print(buyandsellStock([2,3,5,6,7]))



        

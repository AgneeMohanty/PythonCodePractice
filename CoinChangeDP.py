#Given an array with N distinct coins and a target. We have infinite supply of each coin denomination. We need to find the number of ways we sum up the coin values to give us the target.Each coin can be used any number of times
#The constraints given need to be observed as they are essential in dp problems(the minimum coin denomination is 1 and we need to return 0 if there isnt a possible way)
#If we look from the angle of target, the choice we have at each step(each index which means each coin denomination as array of coin values is given here)(like we had 2choices at each step for stair problem) is to either take a coin or not take it.
#Also we have to maintain 2 variables, one is index  and one is target
def coinchange(arr,target):
    index=len(arr)-1
    def coinpossible(index,target):
        #Since we keep subtracting from target and keep decrementing index, the base case will be where for sure target will be zero if we have found proper coin denominations or else either target or index will have reached a value less than 0
        if(target==0):
            return 1
        if(index<0) or (target<0):#means we have reached negative index or negative target that means no way was possible
            return 0
        take=coinpossible(index,target-arr[index])#We stay at the same index because we can still take that index again and subtract the value of coin from target
        nottake=coinpossible(index-1,target)#The target remains same and we move to the previous index
        ways=take+nottake
        return ways
    return coinpossible(index,target)
print(coinchange([1,2,5],5))
    
    

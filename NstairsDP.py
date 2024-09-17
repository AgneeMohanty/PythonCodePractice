#Given a number of stairs. Starting from the 0th stair we need to climb to the "Nth" stair. At a time we can climb either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.
#Now, we know that at each step we can go either one or 2 steps.
def stair(n):
    
    if(n==0 or n==1):
        return 1#if we have to go to the 1st or 0th step we can do so in only one way
    else:
        return stair(n-1)+stair(n-2)#all possible combinations after taking 1 step at last plus all combinations after taking 2 steps at last
    #We notice that here we are calculating the steps backward from the nth index
print(stair(4))

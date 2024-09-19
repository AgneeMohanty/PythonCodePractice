#Given an array , find the longest increasing subsequence.A very important point to note is that the subsequence need not be consecutive,it just needs to be increasing , this is the reason dp works here
#Here we will use DP.
#At each step we have 2 choices either to take or not take an element
def LongestIncreasingSubsequence(arr:list[int])->int:
    n=len(arr)
    def func(index,prev_index):
        #The base case will be the last element, that is when index will be equal to n and we must return 0 as there are no elements to take as index will traverse from 0 to n-1
        if(index==n):
            return 0
        notTake=0+func(index+1,prev_index)#if we dont take an element, then the current index is incremented to +1 and prev_index remains same.
        #instead of prev_index = -1 we can directly give -1 value of prev_index in function call#We initialise prev_index to keep track of the index of previous index which will let us decide whether to take an element or not.
        #Since prev_index is -1 at first, we will always take the first element of array, which you can understand from the next step
        take=0#initialising a value for take to avoid error
        if(prev_index==-1 )or( arr[index]>arr[prev_index]):#This condition ensures that we take elements that are striclty greater than the last element
            take = 1+func(index+1,index)#if we take an element,we call the function for next element also, the current index becomes the previous index for the next call.
        return max(notTake,take)#Since we need the longest subsequence we will return the max of choices.
    return func(0,-1)
print(LongestIncreasingSubsequence([5,4,11,1,16,8]))
    

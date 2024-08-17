#Given an unsorted array of integers ,find the length of the longest consecutive elements sequence
#Easy solution
def longestConsecutiveSequence(nums:list[int])->int:
    nums.sort()
    maxcount,count=0,1 #count is initialised as 0 because when we are checking the element and one before it while iterating, so minimum sequence length is 1, also this will help if no ssequence of length 2 or more is there, then the longest sequence will be length 1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]+1:
            count+=1
        
        elif count>maxcount:#The moment when the element we r checking isnt consecutive of its previous element,assign count to maxcount.and reset count to 1.
            maxcount=count
            count=1
    return maxcount
print(longestConsecutiveSequence([1,2,3,4,100,200]))
    

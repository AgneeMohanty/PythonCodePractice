#Given an unsorted array of integers ,find the length of the longest consecutive elements sequence
#taking a look at the array we notice that if we could identify the sequences, then we could work on them
#But how will we identify how a sequence starts
#in the array[1,2,3,4,100,500] we notice that the elements from which the sequence starts, such as 1, 100 and 500
#dont have a left neighbor that is their previous consecutive element.
#1 doesnt have 0 in the array, 100 doesnt have 99 in array and 500 doesnt have 499
#This can be done O(n) time by iterating through each element and checking if its start of a sequence and if not does it have a predecessor in the  array(count+1)
def longestConsecutive(self, nums:list[int])->int:
    numSet = set(nums)
    longest =0
    for i in nums:
        #Check if its the start of a sequencr
        if (n-1) not in numSet:
            length=0
            while(n+length) in numSet:
                length+=1
            longest = max(length,longest)
        return longest

#Given an array nums of n integers, are there elements a, b, c in nums such that a+b+c=0? Find all unique triplets in the array which gives the sum of zero.
#The array may have negative numbers and repeatitions
#We cant have duplicate triplets or duplicates in our triplet solution.
#lets do this the easy way first,
#We'll iterate through every possible 3 element combination and check if sum is equal to zero or not
import itertools
def threeSum(nums:list[int])->list[list[int]]:
    res =[]
    n=len(nums)
    flag=True
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (i<n )and (j<n )and (k<n):
                    
                    if (nums[i]+nums[j]+nums[k])==0:
                        x=[nums[i],nums[j],nums[k]]
                        y=list(itertools.permutations(x))
                        
                        for l in y:
                           if l  in res:
                               flag=False
                               
                               
                        if flag==True:
                            res.append(x)
                           

    
    return res
print(threeSum([-1,2,8,4,-1,3,1,-2,-3]))

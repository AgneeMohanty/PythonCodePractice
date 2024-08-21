#Given n non -negative integers a1,a2,-----an where each represents a point at coordinate (i,ai),n vertical lines are drawn such that the 2 endpoints of the line are
#(i,ai) and (i,0).Find two lines which togethere with the x-axis forms a container, such that the containeer contains the most water.
def waterContainer(nums:list[int])->list[int]:
    n = len(nums)
    maxarea=0
    for i in range(n):
        for j in range(i+1,n):
            if (i<n) and (j<n):
                area=nums[i]*(j-i)
                if area>maxarea:
                    maxarea= area
                    x= [nums[i],nums[j]]
    
    return x
print(waterContainer([1,2,4,4,2,0,2,3]))

#Find the second largest number in an array
def secondlargest(nums:list[int]):
    maxelement=0
    secondmax=0
    for i in nums:
        if i >secondmax:
            if i> maxelement:
                secondmax=maxelement
                maxelement=i
            elif i !=maxelement:#i<=maxelement also i is a distict element(for cases where 2 largest are there of same values)
                secondmax=i
    return secondmax
print(secondlargest([1,2,3,4,5,4,3,8,9]))
print(secondlargest([1,2,3,4,5,8,8]))                
        
            

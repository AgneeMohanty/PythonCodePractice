#Given n non negative integers representing an elebation map where  the width of each bar is 1. Compute how much  water it can trap after raining.
#If we draw a diagram we find a histogram like figure.
#The array is given as[0,2,1,3,0 1,2.....].
#The algorithm to solve this problem is that for each index we can decide the water it stores by
#the formula min(L,R)-element.Here L ,R are the greatest elements to the left and right of an element respectively
#we take the minimum of L and R and from it subtract the element itself
#if we get a positive integer then that is the amount of water it can hold, if we get a negative one, it means it can hold 0 water.
#This algorithm also gives us the right value for the left and right elements as well
def trapRainwater(nums:list[int])->int:
    #we can maintain 2 arrays for maximum element to left and right
    n=len(nums)
    #maxleft=[]
    #maxright=[]
    minofleftandright=[0]*n
    res=[0]*n
    
    #minofleftandright[n-1].append(0)
    #minofleftandright[0]=0
    for i in range(0,n):
        if (i<1)or(i>=n-1):
            minofleftandright[i]=0
        if((i!=0) and (i!=n-1)):
            minofleftandright[i]=min(max(nums[:i]),max(nums[i+1:n]))
    for i in range(0,n):
        if minofleftandright[i]-nums[i]<0:
            res[i]=0
        else:
            res[i]=(minofleftandright[i]-nums[i])
            
    print(res)
    return sum(res)
print(trapRainwater([0,1,0,2,1,0,1,3,2,1,2,1]))
        

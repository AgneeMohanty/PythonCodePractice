#Binary search algorithm
def binsearch(x:int):
    num=[1,2,3,4,5,6,7,8]
    num=sorted(num)
    low=0
    high =len(num)-1
    
    def search(low,high):
        if high>=low:
            mid=(low+high)//2
            if num[mid]==x:
                return mid
            elif x<num[mid]:
                return search(low,mid-1)
            else:
                return search(mid+1,high)
        else:
            return -1#If none of the conditions were met while high>low
    return search(low,high)
print(binsearch(3))

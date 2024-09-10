#Maximum product subarray-to find the subarray that has maximum product in an array with negative and positive integers
#We'll follow the same approach as the max sum subarray question.
def maxproductSubarray(nums:list[int])->int:
    n= len(nums)
    lst=[]
    for i in range(n):
        for j in range(i+1,n):
            lst.append(nums[i:j])
    min_int = float('-inf')
    subarray=[]
    for i in lst:
        prod1=1
        for j in i:
            prod1*=j
        if prod1>min_int:
            min_int=prod1
            subarray=i
    print(prod1)
    print(subarray)
    return prod1
maxproductSubarray([1, -2, 3, -4])

#Given an array nums , return an array such that answer[i] is equal to the product of  all  the elements of nums except nums[i]
#This can be solved directly using brute force approach, either we can use the division where we first calculate the product of the entire array and for each element we just divide the product by that number to get answer[i] for that position
#or we can even directly iterate through all manually and keep multiplying

def productofArrayExceptSelf(nums:list[int])->list[int]:
    answer=[] #Empty list answer is initialised or created
    product=1
    for i in nums:
        product*=i

    for i in range(len(nums)):
        answer.append(product/nums[i])

    return answer
print(productofArrayExceptSelf([1,2,3,5]))

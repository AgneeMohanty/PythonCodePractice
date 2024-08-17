#TwoSumII In this we are given a sorted array and a target and we need to find 2 numbers such that they add up to target.The function returns the indices of the two numbers such that they add up to the target where index 1 must be less than index2
#There is exactly one solution and we cant take the same element twice
#In the easy method, for each element we can check if the array has target-element,also it'll be easy since only one such pair exists
#After this we can also try to analyse a solution with hashmap
def TwoSum2(nums:list[int],target:int)->list[int]:
    for i in nums:
        if(target-i) in nums:
            return [nums.index(i),nums.index(target-i)]

print(TwoSum2([1,2,3,4],4))

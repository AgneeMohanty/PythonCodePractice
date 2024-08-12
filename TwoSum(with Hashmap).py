#Return the index of the 2 numbers in array that add up to give a number k(target),
#also its given that exactly one such pair exists
#Brute force , we take each element and iterate through all elements after it to check the sum.
#Instead We could use a hashmap where key is the element and the value is the index of that element.
#we also notice that if an element e + another element f ==k , then if we are iterating over e
#we can check if e-k exists anywhere in the array, we can return its index.
#But here also another problem lies , first we have to fill the hashmap then we need to check through it , instead we use a clever solution of filling the hashmap simultaneously while checking the existence of the element k-e for a elemente.
def twoSum(nums:list[int],target:int)->list[int]:#we have to return a pair of inidices
    prevmap ={}#we are creating an empty hashmap ,naming it prevmap because at each step we will be checking all the keys or elements that have been added to hashmap before it.
    for i,j in enumerate(nums):#enumerate creates a dictionary with keys = index of element and value = element
        diff=target-j
        if diff in prevmap:
            return [prevmap[diff],i]#prevmap[diff] will return index of the second element from hashmap and i will give the index of the first element
        prevmap[j]=i#This will add the element to prevMap if the other element is not found
    return # if we iterate through the entire list without success.

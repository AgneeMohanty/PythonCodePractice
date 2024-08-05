def containsDuplicate(lst)->bool:
    hashset = set()# in python we can directly create hashset with set,
    for i in lst:
        if i in hashset:
            return True#if i in hashset it will ignore rest of function and return true as result, but only if its false till the last iteration, it will proceed to last part of code where it will return false.
        hashset.add(i) #This is the part which runs if  "if" is unsuccessful,we add the element to the hashset
    return False

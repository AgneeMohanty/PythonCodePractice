def AnagramWithoutHashMap(s:str,t:str)->bool:
    # We can simply sort the 2 strings and compare them ,this will return false even if they are not of equal length
    if sorted(s)==sorted(t):
        return True
    return False
#AnagramWithoutHashMap('agnee','eenga')

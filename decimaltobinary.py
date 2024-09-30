#Convert decimal to binary format
def decimaltobinary(n:int):
    res=0
    place=1
    while(n>0):
        rem=n%2
        res=res+rem*place
        n=n//2
        place=place*10
    
    return res
print(decimaltobinary(15))



        

#Replace 1s with 0s in integer without using any string to integer conversions
def replacewithzero(n:int):
    res=0
    place=1
    while(n>0):
        rem=n%10
        if(rem==1):
            res=res+0*place
        else:
            res=res+rem*place
        n=n//10
        place=place*10#The value of the place multiplies by 10 at each step
    return res
print(replacewithzero(213))

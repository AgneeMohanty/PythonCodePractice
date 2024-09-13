#Write a function that takes the binary representation of a positive integer and returns the number of set bits(1) it has (also known as the Hamming weight).
#Input will be a 32 bit integer for example 00000.......1101
#The way we can identify 1 is by % the entire number by 2,if the last digit is 1,it will give reamainder 1 else 0.
#After we have identified a bit(last bit) we can bring the previous bit to its place by right shifting the number by 1
#This can go on until all 1s are identified and removed after which the number will become 0
def onebits(n):
    count=0
    while(n!=0):#till all 1s are not shifted
        if(n%2)!=0:#last bit is 1
            count+=1
        n=n>>1#Right shift n by 1 bit
    return count
print(onebits(1101))

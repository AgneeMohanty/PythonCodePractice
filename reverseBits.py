#Reverse bits of a given 32 bits unsigned integer.For example an integer is given as 24742703205787..... then reverse it as .........724742
def reversebits(n):
    s=''
    b=str(n)#Taking the 32 bit integer in string format
    r=b[::-1]
    l=len(b)#for use in loop ahead
    print(r)
    #For converting the string binary format into integer format,
    binary=0
    for i in range(0,l):
        number=int(n[i])
        binary+=number*(2**(i-1))
print(reversebits(10100101000001111010011100))

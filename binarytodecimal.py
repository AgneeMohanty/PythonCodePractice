#Converting binary to decimal
def converttodecimal(n):
    i=0
    decimal=0#To store the result number
    while(n>0):
        rem=n%10#To get the last digit
        decimal+=rem*(2**i)
        i+=1
        n=n//10
    return decimal
print(converttodecimal(1000))
        


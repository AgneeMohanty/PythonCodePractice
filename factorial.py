#Write a code to find the factorial of a number
def fact(n):
    #Defining the base cases
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

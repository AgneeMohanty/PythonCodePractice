#Given an integer n , return an array ans of length n+1 such that for each i, ans[i] is the number of 1's in the binary representation of i.
#We could use the same formula that we used for calculating the number of set bits in a binary number
#The catch here is that the numbers are not gonna be in binary format.
#But we have a formula to find number of 1s in the binary form of any integer
#If we keep modulus  the number by 2,we get the remainder digit as 0 or 1 at each step.Then to remove the last digit we perform an integer division on the number 
#For example 3 has 2 1s,->3%2=1 then 3 ->3//2=1 and 1%2 =1 again 1//2=0,till 0 the modulus with 2 gave 2 ones so count is 2.
def countingbits(n):
    lst=[0]*(n+1)
    for i in range(0,n+1):
        count=0
        temp=i#Sinc the value of i is being altered in the below loops, we store the value of i in temp for inserting the count into ith index
        while(i!=0):
            if i%2==1:
                count+=1
            i=(i//2)
        lst[temp]=count
    return lst
print(countingbits(5))
        

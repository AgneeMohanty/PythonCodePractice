def longestnumberpalindrome(num:list[int]):
    res=0#For storing the number that is the largest palindrome
    maxcount=0
    for i in num:
        n=i
        x=0
        count=0
        #All the above values we need separate for each element ,so we define them after the loop
        while(n>0):
            x=10*x+(n%10)
            n=n//10
            count+=1
        if x==i:
            if count>maxcount:
                res=i
    return res
print(longestnumberpalindrome([1234,2332,223322,233212332]))

#Given a string in the form, aabbbccdddd, we need to convert it into string of format "a2b3c2d4" also if frequency of any letter is 1 no need to mention its count
def code(s:str):
    res=""
    count=1
    for i in range(len(s)):
        if s[i]==s[i+1]:
            count+=1 #As we can see here we are counting one step ahead, so if the next letter is not same we can detect it
        else:#in the else condition we encounter a different letter ,so it would be wise to append the previous letter and count to the result string
            if count==1:#If count is 1 upon encountering a different letter we just add the letter to result without adding its count
                res+=s[i]
            else:
                res+=s[i]
                res+=str(count)
                count=1#Also we will reset the value of count to 1 on encountering a different letter
    return res
print(code(abbcccdddd))

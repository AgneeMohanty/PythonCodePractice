#Longest substring without duplicates, for example in "abcabcbb", the longest such
#substring is abc.What we can do is check every possible substring, that is iterating through the string, for each letter we can check every possible substring of that letter with the letters after it
#But suppose we find in the above example while checking for first a  that after 4 elements a is again repeated then we dont need to unnecessarily check the remaining possible substrings of a that come after it.
def longestSubstring(s:list[str])->str:
    n = len(s)
    trackerlst=[]#We can append the letters in list for each iteration of i  and update the list for max length of list
    maxlength=0
    res=''#string which will store the substring with max length
    for i in range(n):
        trackerlst.append(s[i])
        for j in range(i+1,n):
            if s[j] not in trackerlst:
                trackerlst.append(s[j])
            else:
                break
        if len(trackerlst)>maxlength:
            maxlength =len(trackerlst)
            res=''#Clears the string from previous max
            for i in trackerlst:
                res+=i
        trackerlst.clear()
        return res


print(longestSubstring("abcabcbb"))
            
        

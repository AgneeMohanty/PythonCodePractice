#Given 2 strings s and t return true if t is an anagram of s and false otherwise
#it means whether we can create t using all characters of s.
#Here also we can use hashmaps,we'll create 2 hashmaps one for s and one for t, where the key of the map will be the alphabet and value will be the frequency of that alphabet.
#since the character itself is the key, we can write hashmap[s[i]] to access the corresponding value of the key s[i]
#Hashmap is used to store key-value pairs ,it allows efficient retrieval of values based on keys
def isAnagram(s:str,t:str)->bool:
    if len(s)!=len(t):
        return False#no possibility of anagram if strings are not of equal length so directly return false
    countS,countT = {},{} #2 hashmaps are created
    for i in range(len(s)):
       # countS[s[i]]=1+countS[s[i]]   this adds 1 to the value of a character in the hashmap whenever that character is encountered,
       countS[s[i]] = 1 + countS.get(s[i],0)# this means that if the key doesnt exist it wont show error unlike the above case, instead it will return default value 0
       countT[t[i]] = 1 + countT.get(t[i],0)

    for c in countS:# here we are iterating through the keys in the hashMap
        #if countS[c]!=countT[c] would be okay but keyerror if key doesnt exist
        if countS[c]!=countT.get(c,0):
            return False

    return True #if function comes till this, then return True,since through the entire function we gave conditions for false

#Group Anagrams
#Given an array of strings ,group the anagrams together.You can return them in any order
#ex input = [eat,tea,ate, bar,arb] output = [[eat,ate,tea],[bar,arb]]
# if we find out which letter from a-z are present in a string and how many times, then we can compare other strings for anagrams
#Here we will use hashmap, where the dictionary with alphabet and its frequency will be the key and its value will contain all strings that have the same letters
#so basically in the anagrams we will be mapping character count to the list of anagrams.
#Dictionary is the same as hashmap , that is why we define it as {}
from collections import defaultdict
def groupAnagram(strs:list[str])->list[list[str]]:
    result={}#Create an empty dictionary or hashmap
    
    for s in strs:
        count=[0]*26# a........z 26 space lists with all value 0 is created for each word in strs list
        
        for i in s:#i in s means that for each alphabet of each word s in strs
            count[ord[i]-ord['a']]+=1#increment count of respective alphabet index between 0 and 25
            #ord[i]-ord['a'] gives the index of a element from 0 to 25,do yourself and see(a will be 97-97=0 , b will be 98-97=1......so on upto 25)

    result[tuple(count)].append(i)#now for a particular count, the count will be added to key and that word will be added to value, if count already present ,a new word comes with same alphabet frequencies will be added to tha value list for that count key
    return result.values()
            
        

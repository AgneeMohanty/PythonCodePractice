#Given a string s, determine if its a palindrome, considering only alpahnumerica characters and ignoring cases
#The string may contain capital letters, symbols, spaces too
#example-"A man , a plan, a canal: Panama"
#first lets solve using the easy technique
def isPalindrome(string:str)->bool:
    str=""
    for i in string:
        if i.isalnum():
            str+=i.lower()
    return str==str[::-1]
       
print(isPalindrome("Agnee , eenga"))

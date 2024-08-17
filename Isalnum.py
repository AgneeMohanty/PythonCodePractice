#Creating the alnum method manually
def isalnum(s):
    return(ord('a')<=ord(s)<=ord('z')
    or ord('A')<=ord(s)<=ord('Z')
    or ord('0')<=ord(s)<=ord('9'))

print(isalnum('a'))

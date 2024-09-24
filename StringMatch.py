#Code to check if two strings match where one string contains wildcard characters
def match(a:str,b:str):
    c=''
    d=''
    for i in a:
        if i.isalpha():
            c+=i
    for i in b:
        if i.isalpha():
            d+=i
    if c==d:
        return True
    else:
        return False
print(match('Agnee1343@#^%^','Agnee'))

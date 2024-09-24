#Find non repeating  characters in a string
def nonrepeatingchars():
    s="Agnee"
    lst=[]
    for i in s:
        count=0
        for j in s:
            if i==j:
                count+=1
        if count>1:
            if i not in lst:
                lst.append(i)
    return lst
print(nonrepeatingchars())

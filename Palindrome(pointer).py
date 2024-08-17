#We will be solving this without using any extra memory space,
#Here well be using 2 pointers one start and one at end,we will be incrementing start one and decrementing end one, and checking if the elements at those pointers are equal
#This will go on till the pointers pass each other(in case of even elements) or if they point to the same index(in case of odd elements)
#of course we have to take care non alphanumeric values
def isPalindrome(String:str)->bool:
    i,j=0,len(String)-1
    while(i<j):
        if(i<j):#So we dont get index out of bounds exception
            if not String[i].isalnum():
                i+=1
                continue
            if not String[j].isalnum():
                j-=1
                continue
            if String[i].lower() != String[j].lower():
                return False
            i+=1
            j-=1
    return True
print(isPalindrome("Agnee, eeng a"))
                
            

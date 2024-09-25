#Circular rotation of an array by k elements
#This means that each element shifts by k positions

def circularrotation(num:list[int],k:int):
    n=len(num)
    num2=[0]*n
    for i in range(len(num)):
        if(i+k)<len(num):
            num2[i+k]=num[i]
        else:
            num2[(k+i)-n]=num[i]#To handle values greater than the length of array
    return num2
print(circularrotation([1,2,3,4,5,6,7],3))

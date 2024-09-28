#Calculate the frequency of element in an array (without dict)
def frequency(num:list[int]):
    #We will maintain another array which will contain flags for each element telling us if we visited it or not for duplicate elements
    #here we wont be storing the counts anywhere rather, in every iteration we will be printing the count value with the element
    #The array is gonna be [10,23,10,22,23] So we wont be taking 10 for the second time
    n= len(num)

    num2=[False]*n
    for i in range(n):
        if(num2[i]==False):
            count=0
            for j in range(n):
                if(num[i]==num[j]):
                    num2[j]=True
                    count+=1
            print("frequency of ",num[i],"is",count)
                
frequency([10,12,12,10,20,20])          
               
               
                
    

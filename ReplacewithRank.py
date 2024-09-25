#Write code to replace element in an array with its rank in the array
#Rank in array will be the position of element in the sorted array
def replacerank(num:list[int]):
    num2=sorted(num)
    for i in range(len(num)):
        for j in range(len(num2)):
            if num[i]==num[j]:
                num[i]==j+1#As the indexing starts from 0 but rank will start from 1
    return num
print(replacerank([1,2,4,3]))









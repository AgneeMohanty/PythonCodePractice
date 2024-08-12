#Given an integer array nums and an integer k,return the k most frequent elements, You may return the answer in any order.
#Here k most frequent means if 2 elements occur thrice which is the maximum times and 3 elements occur twice, and one element occurs once, k=2 means that we will return all elements with top 2 frequencies, that is thrice and twice , i.e. 5 elements
# This can be solved in linear time by creating a hashmap(with elements as key and their counts as values)
#another list is created with space 0 to n+1(size of array+1)( this is actually frequency count and cant be more than n+1(i.e the size of the array))
#In the dictionary The count is the key and the value is the list of elements that have the corresponding frequency count
#In the list, we put the elements in the index which is same as the count.
#Upon being asked about the k top frequent values , we can start looking from the end of the list starting count key from n (largest frequency).

def kfrequent(l:list[int],k:int)->list[int]:
    count={}
    freq =[[]for i in range(len(l)+1)]#since frequency array will contain list of elements for each index, we define it as a list of n+1 lists
    
    for n in l:
        count[n]=1+count.get(n,0)#it could be 1+count[n] but if key of n is empty at first it will show error.

    for n,c in count.items():
        freq[c].append(n)

    res =[]
    for i in range(len(freq)-1,0,-1):#iterating the frequency array from end to find the most frequent
        for n in freq[i]:
            res.append(n)
            if len(res)== k:
                return res
    #to access k first elements of the list of keys from Counter dictionary which automatically arranges elements from most frequent to least.
print(kfrequent([1,1,12,2,2,2,3,1],2))    
    
        
    


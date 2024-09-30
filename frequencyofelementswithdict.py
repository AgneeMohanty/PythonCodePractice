#finding the frequency of each character in array using dictionary
def frequency(num:list[int]):
    freq_dict={}
    for i in num:
        if i in freq_dict:
            freq_dict[i]+=1
        else:
            freq_dict[i]=1
    return freq_dict
print(frequency([1,2,2,3,3,3,4,4,4,4]))  

#Design an algorithm to encode a list of string.The encoded string is then sent over the network and is decoded back to the original list of strings
#Please implement encode and decode
# here the question doesnt want us to create a separate array if possible,but work on that string itself
#Example of encoding-input=["hare","krishna","ram"] encoded format="hare:;krishna:;ram"
#if we join all words together we also need to remember where each word ends or starts to decode them again
#So, one approach is using delimeters such as # or @ to separate each word but the problem is that the words may contain # @ so it will create false decoding
#What we will do is before each word append the number of letters it has ,and put a delimeter between the number and the word to stop reading number when we encounter a delimeter.
#So when we encounter the word #wxyz, we will make it 5##wxyz, here even if the word has the same delimeter it wont be a problem because we know the number of letters and after encountering one # we will take the next 5 letters no matter what they are

def encode(self, strs):#Dont worry about the driver code, just understand the pseudo code
    res = "" #this is the result string which is a empty string to which we will append the elements of strs and put one one delimeter between them
    for i in strs:
        res+=str(len(s))+"#"+s

    return res
        
def decode(self,str):
    res=[]#resulting list
    i=0
    #Now we have to read the length of the string then read from delimeter onwards to that much length
    #this is the reason we use a marker i to mark to mark the starting point(length) and j for starting point of string
    while i <len(str):
        j=i
        while str[j]!='#' :#in case of 4#harekrishna,4 is marked by i and j adds on until it finds # So j points at the #
            j+=1
        length = int(str[i:j])#i is the index of first str length,j is the index of  delimeter,so str[i:j] will give us 4 for above example and we can convert it to integer
        #length will give us the size of the string since one extra length is added as we start from the str len number itself , also one extra is less as last index is not included in splicing
        res.append(str[j+1:j+1+length])#From j to j+length of word
        i=j+1+length #(i will move to end of appended word)(or start of second word that is its length)
    

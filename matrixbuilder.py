#Create and add a 3X3 matrix .
def creatematrix():
    lst=[]
    for i in range(3):
        lst.append([0,0,0])
    return lst
print(creatematrix())
#lets add one matrix to another 3X3 matrix
def addmatrix():
    lst1=[[1,1,1],[1,1,1],[1,1,1]]
    lst2=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            lst1[i][j]+=lst2[i][j]
    return lst1
print(addmatrix())

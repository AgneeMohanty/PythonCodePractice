#Find symmetric pairs in an array such as [(1,2),(2,1),(3,4),(4,5)]
def symmetricpair(nums:list[tuple[int]]):
    res=[]
    res2=[]
    for i,j in nums:
        res.append((i,j))
        if (j,i) in res:
            res2.append((i,j))
    return res2
print(symmetricpair([(1,2),(3,2),(2,1),(2,3),(3,1)]))

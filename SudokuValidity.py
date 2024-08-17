#Determine if a 9X9 Sudoku is valid. Only the filled cells need to be validated according to the following rules
#Each row and column must contain digits 1-9 without repeatition
#Each of the 3X3 sub-boxes must contain digits 1-9 without repeatition
#Note that 1-9 means that any number between 1-9 and not all, so it may contain only 7 and no repeatition then it is valid.
#Basically we are going to create a hashset for each column and each row to check the row and column conditions.
#But for sub squares we will be using a different method. Suppose we number rows and columns of sudoku from 0 to 8 . Then the boxes can be (0,3),(5,6) and so on. Now we will use a technique where
#for first second and 3rd  3 indices , we will label them  0 ,1 and 2 respectively. For example both along the rows and columns we will label 0,1,2 as 0 , then 3,4,5 as 1 , and finally 6,7 ,8 as 2.
#This way each of the 9 subboxes can be referred to as a pair of 2 numbers such as (0,1), (2,1) and so on.
#Now we must understand how we got these 0,1, and 2 . We can see that if we do integer division of indices in a subbox by 3, we get exactly the subbox address of that index (according to 0,0 or 1,0 ) .
#for example a box has index(1,2) . Then (1/3,2/3) will give us in which subbox it lies.(1/3=0,2/3=0) ->(0,0), in this way we can find the subbox address of every index
#The hashmap for the subboxes will contain a pair of indices as key  and the subbox as the value.
from collections import defaultdict
def validSudoku(self,board:list[list[str]])->bool:#Sudoku is a list of lists(str as some are empty)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    sub_squares = collections.defaultdict(set)#Basically we create 3 dicitionaries

    for i in range(9):
        for j in range(9):
            if element[i][j]==' ':
                continue#Function continues as usual if it encounters a empty space
            if(element[i][j]  in rows[i]
               or element[i][j]  in cols[j]
               or element[i][j]  in sub_squares[i//3][j//3]):
                return False#even if once we find a invalid element , the sudoku is invalid
#if element not in row column or subsquare add it to value of row dict, col dict and subsquare dict for future elements checking
        
            cols[j].add(element[i][j])
            rows[i].add(element[i][j])
            sub_squares[(i//3,j//3)].add(element[i][j])
            #above we can notice that cols and rows have keys 0 to 9 but subsquare has a pair of elements as keys(row//3,col//3)
    return True#if anywhere above the function doesnt return False , then only control reaches here
        


    
            
    


    

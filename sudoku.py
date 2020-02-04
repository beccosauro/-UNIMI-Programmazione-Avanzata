'''
Exercise 1: Sudoku's Generator.
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, 
each row, and each of the nine 3×3 sub-grids that compose the grid contains all of the digits from 1 to 9. The puzzle setter provides 
a partially completed grid, which typically has a unique solution. There are 6,670,903,752,021,072,936,960 possible sudokus. 
By reducing the grid size to a 4×4 and considering only figures from 1 to 4 you get a simplified version of the sudoku with only 4 
sub-grids 2×2 that admits much less solutions.

The exercise consists of writing a generator function (sudoku) that at each call returns a valid (and different) sudoku 
solutions for the simplified version of the problem. Note that not all combinations are valid solutions. 
The returned combination should be a list of lists where each entry will represent a row of the grid.

Note that the solutions which calculate the combinations via a nested loops are considered wrong.
'''
import itertools,functools
flatten = lambda l: [item for sublist in l for item in sublist]

def getSubMatrix():
    matrix = [[x for x in range(4)] for y in range(4)]
    diagonaLeft = [list(itertools.product((x,x+1),repeat=2)) for x in range(0,3,2)]
    diagonalRight = [[x for x in list(itertools.product((0,1,2,3),repeat=2)) if x not in flatten(diagonaLeft)][i:i+4]  for i in range(0,7,4)]
    [diagonaLeft.append(x) for x in diagonalRight]
    return [[matrix[x[0]][x[1]] for x in pos] for pos in diagonaLeft]

def sudoku():
    combinations = list(itertools.permutations([list(x) for x in itertools.permutations([1,2,3,4],4)] ,4))
    rowCond = lambda matrix : functools.reduce(lambda x,y: x and y ,map(lambda y:len(set(y)) == 4,matrix))
    columnCond = lambda matrix : functools.reduce(lambda x,y: x and y ,map(lambda y:len(set(y)) == 4,zip(*matrix)))
    #TODO subMatrixCond = lambda comb : 
    for m in combinations:
        if rowCond(m) and columnCond(m): print (m)
        break
    
getSubMatrix()


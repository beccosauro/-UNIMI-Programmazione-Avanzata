'''
Ruzzle is a grid (4×4) based game where each element of the grid is a letter and the aim of the game consists in determining all the possible English words out of all possible 
paths in the grid (where a path is a sequence of adjacent grid elements).

The exercise consists of writing a function ruzzles that calculates all the English words hidden in a given grid with the following simplifications/constraints:

- the minimum length for a word is 3 characters;
- an entry is considered adjacent to another if it is immediately at left, at right, above or below it (no diagonals are considered); note that a word can also be hidden in the
 grid in its reversed form (i.e., it can be read from right to left);
- no entry can be considered twice in the same word;
- the words should be checked against this dictionary;
- the list of resulting words must be alphabetically sorted;
- The input is a list of 4-character strings where each string represents a row in the grid and their position in the list mimic the position in the grid.'''
import itertools
dictionary = open("dictionary.txt").read()
isWord = lambda w: w in dictionary
getWord = lambda pos: "".join([input[x[0]][x[1]] for x in pos])
input, size = ["is","to"],2

positions = list(itertools.product(range(size),repeat=2))
movements = [x for x in itertools.product(range(-1,2),repeat=2) if sum(x)==1 or sum(x)==-1]
sumTuple = lambda x,y: tuple([sum(x) for x in zip(x,y)])

def getNeighbour(pos,seen):
    return [sumTuple(pos,x) for x in movements if 0<=sumTuple(pos,x)[0]<size and 0<=sumTuple(pos,x)[1]<size and sumTuple(pos,x) not in seen]

def getReverse(word):
    c= []

text=set()
def rec(pos,seen):
    neigh=getNeighbour(pos,seen)
    if len(neigh)==0:
        seen.append(pos)
        text.add(getWord(seen))
    else:
        seen.append(pos)
        for p in neigh:
            rec(p,seen.copy())
        
for p in positions:
    rec(p,[])

print(text)

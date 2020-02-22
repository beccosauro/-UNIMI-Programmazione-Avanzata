import itertools

legalPos = lambda x, seen : 0<=x[0]<matrixSize and 0<=x[1]<matrixSize and x not in seen
sumTuple = lambda x,y: tuple([sum(x) for x in zip(x,y)])
getWord = lambda pos,input: "".join([input[x[0]][x[1]] for x in pos])

def getNeighbour(pos,seen):
    return [sumTuple(pos,x) for x in movements if legalPos(sumTuple(pos,x),seen)]

def getReverse(word):
    words = []
    [words.extend([w[x:] for x in range(0,len(w))if len(w[x:])>2]) for w in [word,word[::-1]]]
    return words

def exploreMatrix(pos,seen):
    neigh=getNeighbour(pos,seen)
    seen.append(pos)
    if not neigh:
        [words.add(w) for w in getReverse(getWord(seen,input)) if dictionary.get(w)]
    else:
        [exploreMatrix(p,seen.copy()) for p in neigh]


matrixSize, words = 4, set()
dictionary = {w.strip():True for w in open("dictionary.txt")}
positions = itertools.product(range(matrixSize),repeat=2)
movements = [x for x in itertools.product(range(-1,2),repeat=2) if sum(x)==1 or sum(x)==-1]

input = ["poap", "lkjh", "aswe", "jhnh"]
[exploreMatrix(p,[]) for p in positions]
print(sorted(words))

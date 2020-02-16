import itertools
input, size =["walk", "moon", "hate", "rope"], 4
positions = list(itertools.product(range(size),repeat=2))
movements = [x for x in itertools.product(range(-1,2),repeat=2) if sum(x)==1 or sum(x)==-1]
sumTuple = lambda x,y: tuple([sum(x) for x in zip(x,y)])

dictionary = [w.strip() for w in open("dictionary.txt")]
getWord = lambda pos: "".join([input[x[0]][x[1]] for x in pos])

def getNeighbour(pos,seen):
    return [sumTuple(pos,x) for x in movements if 0<=sumTuple(pos,x)[0]<size and 0<=sumTuple(pos,x)[1]<size and sumTuple(pos,x) not in seen]

def getReverse(word):
    words = []
    [words.extend([w[x:] for x in range(0,len(w))if len(w[x:])>2]) for w in [word,word[::-1]]]
    return words

text=set()
def rec(pos,seen):
    neigh=getNeighbour(pos,seen)
    if len(neigh)==0:
        seen.append(pos)
        [text.add(w) for w in getReverse(getWord(seen)) if w in dictionary]
    else:
        seen.append(pos)
        for p in neigh:
            rec(p,seen.copy())
        
for p in positions:
    rec(p,[])

print(sorted(text))

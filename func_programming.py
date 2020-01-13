### EXCERCISE 1 ###
import itertools,fractions,functools,math
print(sum([x for x in range(1000) if x%3==0 or x%5==0]))

def lcm(a,b):
    return a/fractions.gcd(a,b)*b      

print(functools.reduce(lcm,range(1,20)))
print(functools.reduce(lambda x,y: int(x)+int(y), str(2**1000)))

def fibo():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

counter,number = next((count,num) for count,num in enumerate(fibo()) if len(str(num))>=1000)
print("The %d-th term has %d digits"%(counter,len(str(number))))

### ESERCIZIO 2 ###
import re,collections
def freqs(filename,thresold):
    with open(filename,'r') as file:
        wordList = re.findall(r'(\w+)', file.read().lower())
    
    wordCounter = filter(lambda x: x[1]>=thresold, collections.Counter(wordList).items())
    wordCounter.sort(key = lambda x: x[1], reverse=True)
    print(wordCounter)

#freqs("Enrico_IV.txt",100)

### ESERCIZIO 3 ###
import itertools


def sin(x, n):
    fact = ((n-1)*n if n>1 else 1 for n in itertools.count(1,2))
    x=float(x)
    return sum([x/next(fact) if idx%2!=0 else -1*(x/next(fact)) for idx,_ in enumerate(range(1,n+1),1)])

print (sin(3,20))
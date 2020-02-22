
import string
dictionary = {w.strip():True for w in open("wordlist.txt")}
alpha = list(string.ascii_lowercase)


def chain(start,end):
    pos=0
    
    if start[pos]==end[pos]:
        pos+=1
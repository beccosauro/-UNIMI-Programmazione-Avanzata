import calendar

#### ESERCIZIO 1 ####
nextLeapYear = lambda x: x if calendar.isleap(x) else nextLeapYear(x+1)
print(nextLeapYear(2021))
print(calendar.leapdays(2000, 2050))
print(calendar.day_name[calendar.weekday(2020,1,10)])

#### ESERCIZIO 2 ####
alkaline_earth_metals = {"barium": 56, "beryllium": 4, "calcium": 20, "magnesium": 12, "radium": 88, "strontium": 38}
noble_gases = { "neon": 10, "argon": 18, "krypton": 36, "xenon": 54, "radon": 86,"helium": 2}

print(max(alkaline_earth_metals.values()))
alkaline_earth_metals = {x[0]:x[1] for x in list(alkaline_earth_metals.items())}

merged_gases = {**alkaline_earth_metals, **noble_gases}
print(sorted(merged_gases.items(), key = lambda x: x[1]))

#### ESERCIZIO 4 ####
def identity(size):
    return [[0 if x!=y else 1 for y in range(size)] for x in range(size)]

def square(size):
    return [[x+y for x in range(size) ] for y in range(1,(size*size+1),4)]

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 

def multiply(x,y):
    return [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*Y)] for x_row in X]
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

print(multiply(X,Y))

#### ESERCIZIO 5 ####
import fileinput
def cat(file):
    with fileinput.input(files=file) as f:
        print(*f,"\n")

import os        
def chmod(files):
        [os.chmod(f,0o600) for f in files]
chmod(["testo.txt","cane.txt"])
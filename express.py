ops = {
    "+" : lambda x,y: x+y,
    "/" : lambda x,y: round(x/y),
    "*" : lambda x,y: x*y,
    "-" : lambda x,y: x-y
}    
def calculator(expr):
    l=[]
    for x in expr:
        if type(x)!=list() and x.isnumeric(): l[-1].append(x)
        else: l.append([x])
    
    result = rec(l)
    return result
 
def addResult(lista):
    if len(lista)<2: return lista  
    for idx, x in enumerate(lista):
        if type(x) is str: lista[idx-1].append(lista.pop(idx))
    return lista     

def rec(expr):
    if type(expr[0]) is str: 
        return expr[0]
    else:  
        for idx,x in enumerate(expr):
            if len(x)==3: 
                res = str(ops[x[0]](int(x[1]),int(x[2])))
                print(expr)
                expr[idx]=res
    
        return rec(addResult(expr))
                

if __name__ == "__main__":
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23",
    "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [print(calculator(expr)) for expr in expressions]

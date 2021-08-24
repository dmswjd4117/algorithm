
from itertools import *


def go(index, op, exp):
    if index == 2:
        return str(eval(exp))
    
    res = ""
    
    if op[index] == "*":
        res = eval("*".join([go(index+1, op, splited_exp) for splited_exp in exp.split("*")]))
    
    if op[index] == "-":
        res = eval("-".join([go(index+1, op, splited_exp) for splited_exp in exp.split("-")]))
    
    if op[index] == "+":
        res = eval("+".join([go(index+1, op, splited_exp) for splited_exp in exp.split("+")]))
        
    return str(res)

    
def solution(exp):
    answer = 0
    ops = ["*", "-", "+"]
    ops = list(permutations(ops))
    
    for op in ops:
        res = int(go(0, op, exp))
        answer = max(answer, abs(res))
        
    return answer
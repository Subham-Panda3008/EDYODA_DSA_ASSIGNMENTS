def prefixToinfinix(prefix):
    stack = []
    i=len(prefix) - 1
    while i >=0:
        if not isOperator(prefix[i])
        stack.append(prefix[i])
        i-=1
    else:
        str = "("+ stack.pop() + prefix[i] + stack.pop() +")"

    return stack.pop()

def isOperator(c):
    if c == "*" or c== "+" or c =="-" or c = "/" or c = "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToinfinix(str))
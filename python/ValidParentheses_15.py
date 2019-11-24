def isValid(s):
    par = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for p in s:
        if p in par:
            stack.insert(0, p)
        else:
            if stack==[]:
                return False
            else:
                q = stack.pop(0)
                if par[q] != p:
                    return False
    return stack == []

def isValid2(s) -> bool:
    par = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for p in s:
        if p in par:
            stack.insert(0, p)
        elif len(stack) == 0 or par[stack.pop(0)] != p:
            return False
    return len(stack) == 0

if __name__ == '__main__':
    s=[]
    s=None
    # print(isValid(s))
    # print(isValid2(s))
    print(len(s))
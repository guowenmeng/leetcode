#该题思想：以空间换时间
#   1.判断列表为空：len()==0或者if list_:
#   2.stack[-1],使用-1索引要保证列表不为空，否则报错

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop(-1)

    def top(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        return min(self.stack)

class MinStack2:
    def __init__(self):
        self.data=[]
        self.helper=[]

    def push(self,x):
        self.data.append(x)
        if len(self.helper)==0 or x<=self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])
    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()
    def top(self):
        if self.data:
            return self.data[-1]
    def getMin(self):
        if self.helper:
            return self.helper[-1]

class MinStack3:
    def __init__(self):
        self.data=[]
        self.helper=[]
    def push(self,x):
        self.data.append(x)
        if len(self.helper)==0 or x<=self.helper[-1]:
            self.helper.append(x)
    def pop(self):
        top=self.data.pop()
        if self.helper and top==self.helper[-1]:
            self.helper.pop()
        return top

    def top(self):
        if self.data:
            return self.data[-1]
    def getMin(self):
        if self.helper:
            return self.helper[-1]

obj = MinStack3()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
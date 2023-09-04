
class Stack:
    def __init__(self, stack=None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack
    
    def push(self, v):
        self.stack.append(v)
    
    def peek(self) -> int:
        return self.stack[-1]

    def pop(self) -> int:
        v = self.peek()
        self.stack = self.stack[:-1]
        return v

    def __len__(self) -> int:
        return len(self.stack)

    def __repr__(self) -> str:
        return ','.join([str(v) for v in self.stack])
        
def inverseStack(stk: Stack) -> Stack:
    if len(stk) == 0:
        return
    def pushuntil(leftn, stk, top):
        if len(stk) == leftn:
            stk.push(top)
            return
        next = stk.pop()
        pushuntil(leftn, stk, top)
        stk.push(next)


    ln = 0
    while ln < len(stk)-1:
        top = stk.pop()
        pushuntil(ln, stk, top)
        ln += 1
    return stk 

stack = Stack([1,2,3,4,5])
print(f"inverse stack: {stack} ==> {inverseStack(stack)}")
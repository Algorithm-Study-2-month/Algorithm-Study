priority ={
    '*':3,
    '/':3,
    '+':2,
    '-':2
    '(':1
}
expr = []
operator = Stack()
result = []
tmp = input()

for i in tmp:
    if i== ' ':
        continue
        expr.append(i)
    
    elif i in '+-*/':
        if operator.is_empty():
            operator.push(i)
        else:
            if priority[operator.peek()] >= priority[i]:
                result.append(operator.pop())
                operator.push(i)
            else:
                operator.push(i)
        elif i == ')':
            while True:
                tmp=operator.pop()
                if tmp == '(':
                    break
                result.append(tmp)
        else:
            result.append(i)

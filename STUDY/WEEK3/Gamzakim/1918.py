X = input()  # 연산식 받아오기
stack = []  # 스택 생성
Y = ''

for i in X:
    if i.isalpha():  # 피연산자 확인
        Y += i  # 연산자 'True'일때 Y에 값 넣기
    else:
        if i == '(':  # 괄호일때 스택에 넣기 1순위
            stack.append(i)
        elif i == '*' or i == '/':  # 곱셈 나눗셈 판단 2순위
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # 스택의 맨 윗부분으로 올때까지 pop
                Y += stack.pop()
            stack.append(i)  # 스택에 푸쉬
        elif i == '+' or i == '-':  # 덧셈 뺄셈 판단 3순위
            while stack and stack[-1] != '(':
                Y += stack.pop()
            stack.append(i)
        elif i == ')':  # 닫는 괄호 4순위
            while stack and stack[-1] != '(':
                Y += stack.pop()
            stack.pop()

''' 만약 수식에 괄호가 있다면 다음과 같은 과정으로 처리한다.

1. 여는 괄호('(')이면 push 한다.

2. 닫는 괄호이면 스택의 가장 뒤에 있는 연산자가 여는 괄호가 될 때까지 pop 한 후 출력한다.

3. 스택의 가장 뒤에 있는 연산자가 여는 괄호이면 pop 하여 없애준다.'''

while stack:
    Y += stack.pop()
print(Y)

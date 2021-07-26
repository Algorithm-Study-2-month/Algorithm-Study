import sys

n = int(input())  # 피연산자 개수
X = input()  # 후위 표기식 입력

nums = [0 for _ in range(n)]  # 리스트 생성

for i in range(0, n):
    nums[i] = int(input())  # 피연산자 값 받아오기

stack = []  # 스택 생성

for i in X:
    if i.isupper():  # i가 대문자인지 판단
        stack.append(nums[ord(i) - ord('A')])  # 'o'rd는 유니코드 값을 받는 함수, 피연산자일 때
    else:
        num2 = stack.pop()  # 연산자일 때 스택에 있는 피연산자 두개 pop
        num1 = stack.pop()  # 스택이기 때문에 2번부터 pop

        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '/':
            stack.append(num1 / num2)
        elif i == '*':
            stack.append(num1 * num2)  # 계산 후 스택에 값 push

print(f"{stack[0]:.2f}")  # 마지막 남은 스택 값 소수점 두 자리까지 출력


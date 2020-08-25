# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

if __name__ == "__main__":
    while True:
        stack = []
        line = input()
        result = 'yes'
        if line == '.':
            break
        for i in line:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
                    break
        if stack:
            result = 'no'
        print(result)

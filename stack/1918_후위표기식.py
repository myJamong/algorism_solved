# https://www.acmicpc.net/problem/1918
# 후위 표기식

if __name__ == "__main__":
    line = input().strip()
    stack = []
    result = ''
    priority = {'*':1,'/':1,'+':2,'-':2}
    for c in line:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif c in '*/+-':
            while stack and stack[-1] != '(' and priority[c] >= priority[stack[-1]]:
                result += stack.pop()
            stack.append(c)
        else:
            result += c
    while stack:
        result += stack.pop()
    print(result)

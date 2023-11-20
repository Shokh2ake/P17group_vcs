a = input()

s = []

for i in a:
    if i == '(':
        s.append(i)
    elif i == ')' and s:
        s.pop()
    else:
        print(False)
        break
else:
    print(len(s) == 0)

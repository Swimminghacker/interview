import sys
n = int(sys.stdin.readline().strip())
value = []
def result(n):
    if n == 0 or n == 2:
        return None
    elif n == 1:
        value.append('()')
    else:
        for i in range(n):
            if i == 2:
                value.append('(())')
                value.append('()()')
            else:
                value.append(result(i))
            if n-i == 2:
                value.append('(())')
                value.append('()()')
            value.append(result(n-i))

print(result(n))

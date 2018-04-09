def result(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return result(n-1)+result(n-2)+result(n-3)
print(result(15))

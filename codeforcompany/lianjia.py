import sys
def fei(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return fei(n-1)+fei(n-2)
while True:
    n = sys.stdin.readline().strip()
    if int(n) == 1 or int(n) == 2 or int(n)==3:
        print(0)
    elif n:
        num = 0
        n = int(n)
        result_1 = 1
        result_2 = 2
        result_3 = 3
        for i in range(3,n+1):
            if n < result_3:
                num = i
                break
            else:
                temp = result_3
                result_3 = result_3 + result_2
                result_2 = temp
                
        print(n-num+1)
    else:
        break

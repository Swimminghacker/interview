import sys
value = sys.stdin.readline().split()
n = int(value[0])
k = int(value[1])
num = 0
if k == 0:
    print (n)
else:
    for x in range(n+1):
        for y  in range(2,x):
            if x%y > k-1:
                num = num + 1
    num = num + (1+n-k)*(n-k)/2
    print(int(num))

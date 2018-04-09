import sys
n = int(sys.stdin.readline().strip())
if n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    mod = n%3
    if mod == 0:
        print(3**(int(n/3)))
    elif mod == 1:
        print(3**(int(n/3)-1)*4)
    else:
        print(3**(int(n/3)*2))

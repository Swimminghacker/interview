import sys
n = int(sys.stdin.readline().strip())
myList = [[-1] * n] * n

for i in range(n):
    arr = sys.stdin.readline().split()
    for j in range(len(arr)):
        myList[int(arr[j])][i] = 1
    

print(len(set(a)))

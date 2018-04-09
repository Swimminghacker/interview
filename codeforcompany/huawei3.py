import sys
arr = sys.stdin.readline().split(',')
value = []
for char in arr:
    value.append(int(char))
max_num = -9999999
for i in range(1,len(value)+1):
    for j in range(len(value)-i+1):
        if sum(value[j:j+i]) > max_num:
            max_num = sum(value[j:j+i])
print (max_num)

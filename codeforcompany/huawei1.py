import sys
a = []
for i in range(21):
    a[i] = sys.stdin.readline().strip()
max_sum = 0
index =0
for i in range(17):
    now_sum = a[i]+a[i+1]+a[i+1]+a[i+3]
    if now_sum > max_sum:
        max_sum = now_sum
        index = i
print (index)

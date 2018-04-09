import sys
while True:
    length = sys.stdin.readline().strip()
    value = sys.stdin.readline().split()
    if length == '':
        break
    length = int(length)
    num_arr = []
    for ch in value:
        num_arr.append(int(ch))
    num_arr.sort()
    if length == 1 or length == 2:
        print (1,1)
        
    else:
        difference = []
        for i in range(length-1):
            difference.append(abs(num_arr[i]-num_arr[i+1]))
        difference.sort()
        result1 = difference.count(difference[0])
        if difference[0]==0:
            result1 = int(result1*(result1+1)/2)
        min_num = num_arr.count(num_arr[0])
        max_num = num_arr.count(num_arr[-1])
        result2 = min_num * max_num
        if num_arr[0]==num_arr[1]:
            result2 = int(min_num*(min_num-1)/2)
        print (result1,result2)

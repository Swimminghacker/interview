import sys
string = sys.stdin.readline().strip()
arr = list(string)
n =len(arr)
if n==1:
    print ('false')
else:
    max_i = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            split_arr = []
            for j in range(int(n/i)):
                split_arr.append(arr[i*j:i*j+i])
            if split_arr.count(split_arr[0])==len(split_arr):
                max_i = i
    if max_i == 0:
        print ('false')
    else:
        print (''.join(arr[:max_i]))
        

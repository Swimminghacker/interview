import sys
while True:
    string = sys.stdin.readline().strip()
    if string == '':
        break
    arr = list(string)
    for i in range(len(arr)):
        if 'A'<= arr[i] <='Z':
            arr.append(arr[i])
            arr[i]=''
            print(str(''.join(arr)))

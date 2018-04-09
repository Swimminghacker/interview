import sys
string = sys.stdin.readline()
std_key = 'QWERTYUIOPASDFGHJKLZXCVBNM'+'QWERTYUIOPASDFGHJKLZXCVBNM'.lower()
nat_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
arr = list(string)
for i in range(len(arr)):
    try:
        arr[i] = std_key[nat_key.index(arr[i])]
        print (arr[i])
    except:
        pass
    
print (''.join(arr).strip())

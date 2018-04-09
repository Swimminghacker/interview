import sys
K = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().split()
A = int(arr[0])
X = int(arr[1])
B = int(arr[2])
Y = int(arr[3])
a = []
def getSum(K,X,Y):
    if K == 0:
        a.append((X,Y))
        return 1
        
    if X ==0 and K%B==0 and K/B<Y:
        return jiecheng(K/B,Y)
    if Y == 0 and K%A ==0 and K/A < X:
        return jiecheng(K/A,X)
    if K<0 or (X==0 and Y==0) or (X==0 and K/B != 0)or(Y==0 and K/A != 0) or \
       (X==0 and K/B > Y) or(Y==0 and K/A >X):
        return 0
    return getSum(K-A,X-1,Y)+getSum(K-B,X,Y-1)
def jiecheng(m,n):
    if n<=m:
        return 1
    return n*jiecheng(m,n-1)
getSum(K,X,Y)


def jiecheng2(n,m):
    return jiecheng(1,m)/jiecheng(n,m)

sum_ = 0
has_deal = []
for i in a:
    #print (list(i))
    if list(i) not in has_deal:
        sum_ = sum_ + jiecheng2(i[0],X)*jiecheng2(i[1],Y)
        has_deal.append(i)

def jiecheng2(n,m):
    return jiecheng(1,m)/jiecheng(n,m)
print(int(sum_%1000000007))

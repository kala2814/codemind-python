n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    if(l[i]==0):
        l.remove(0)
        l.append(0)
print(*l)
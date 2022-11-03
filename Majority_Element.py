n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(0,n):
    if l.count(l[i])>n//2:
        m=l[i]
    else:
        pass
print(m)
        
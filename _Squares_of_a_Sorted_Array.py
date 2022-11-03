n=int(input())
l=list(map(int,input().split()))
p=list()
for i in range(0,n):
    p.append(l[i]*l[i])
p.sort()
print(*p)
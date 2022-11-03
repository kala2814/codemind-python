n=int(input())
l=list(map(int,input().split()))
a=int(input())
b=l.index(a)
s=0
for i in range(0,b+1):
    s+=l[i]
print(s)
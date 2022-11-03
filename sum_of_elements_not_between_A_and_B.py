n=int(input())
l=list(map(int,input().split()))
l.sort()
a,b=map(int,input().split())
s=0
for i in range(0,n):
    if(l[i] in range(a,b+1)):
        pass
    else:
        s+=l[i]
print(s)
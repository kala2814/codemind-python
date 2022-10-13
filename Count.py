n=int(input())
l=list(map(int,input().split()))
s=0
g=0
for i in range(0,n):
    if(l[i]%2==0):
        s+=1
    else:
        g+=1
print(s,g)
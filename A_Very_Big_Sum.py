s=0
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    s+=l[i]
print(s)
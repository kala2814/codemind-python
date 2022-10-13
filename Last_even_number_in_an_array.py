n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-1,-1,-1):
    if(l[i]%2==0):
        print(l[i])
        break
    else:
        continue
       
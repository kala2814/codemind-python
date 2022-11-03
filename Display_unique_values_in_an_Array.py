n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    if l.count(l[i])==1:
        c+=1
        print(l[i],end=' ')
if(c==0):
    print('-1')
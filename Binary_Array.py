n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(0,n):
    if(l[i]!=0 and l[i]!=1):
        f=1
        break
if(f==1):
    print('False')
else:
    print('True')
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
s=0
for i in range(0,len(a)):
    if(a[i]>b[i]):
        c+=1
    elif(a[i]<b[i]):
        s+=1
    else:
        continue
print(c,s)
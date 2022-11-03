n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    s+=i
    x=s//n
for j in l:
    if(j<=x):
       c+=1
print(c)
    
    
    
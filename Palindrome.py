n=int(input())
s=0
t=0
t=n
while(t>0):
    r=t%10
    s=s*10+r
    t=t//10
if(s==n):
    print('True')
else:
    print('False')
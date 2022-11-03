s=input()
p=input()
f=0
for i in range(0,len(s)):
    if(s[i]==p):
        f=1
        print("True")
        print(i)
        break
if(f==0):
    print("False")
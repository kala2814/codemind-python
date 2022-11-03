s=input()
d='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0
for i in range(0,len(s)):
    if(s[i] in d):
        c+=1
print(c)
s=input()
k='aeiouAAEIOU'
c=0
for i in range(0,len(s)):
    if(s[i] in k):
        c+=1
print(c)
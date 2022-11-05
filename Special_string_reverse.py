s=input()
l=list(s)
i=0
j=len(l)-1
while(i<j):
    if not l[i].isalpha():
        i+=1
    elif not l[j].isalpha():
        j-=1
    else:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
strOut='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'.join(l)
print(strOut)
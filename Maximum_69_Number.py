n=int(input())
k=str(n)
if '6' in k:
    l=list(k)
    e=l.index('6')
    l[e]='9'
    g=''.join(l)
    print(g)
else:
    print(k)
n=int(input())
for i in range(n):
    s = input()
    c = any(map(str.isdigit, s))
    if(c==True):
        print('Yes')
    else:
        print('No')
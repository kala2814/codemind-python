n=int(input())
l=list(map(int,input().split()))
a=list(set(l))
for i in range(0,len(a)):
    print(a[i],end=' ')
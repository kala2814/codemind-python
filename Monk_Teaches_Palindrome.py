n=int(input())
for i in range(n):
    a=input()
    if(a[::-1]!=a):
        print("NO")
    else:
        if(len(a)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
import math
Number = int(input())
Sum = 0
sqr = math.pow(Number, 2)
while sqr > 0:
    rem = sqr % 10
    Sum = Sum + rem
    sqr = sqr // 10
if Sum == Number:
    print("Neon Number")
else:
    print("Not Neon Number")
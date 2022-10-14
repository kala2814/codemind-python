n=int(input())
for i in range(n):
    string=input()
    if(string==string[::-1]):
      print("True")
    else:
      print("False")
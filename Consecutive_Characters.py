class Solution:
   def solve(self, s):
      if len(s)==0:
         return 0
      s+=' '
      ct=1
      tem=1
      for i in range(len(s)-1):
         if s[i]==s[i+1]:
            tem+=1
         else:
            ct=max(tem,ct)
            tem=1
      return ct
ob = Solution()
str=input()
print(ob.solve(str))

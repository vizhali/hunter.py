vizh1=int(input())
bob1=list(map(int,input().split()))
m1=max(bob1)
a,b=0,0
for i in range(0,len(bob1)-1):
  for j in range(i+1,len(bob1)):
    if abs(bob1[i]+bob1[j])<m1:
      a,b=bob1[i],bob1[j]
      m1=abs(a+b)
print(a,b)

check=int(input())
zero=0
list=list(map(int,input().split()))
new=[]
for i in range(0,check):
    if((list.count(list[i]))>=2):
      if list[i] not in new:
        new.append(list[i])
        zero=1
if(zero==0):
  print("unique")
else:
  for i in range(0,check):
    print(min(new),end=" ")
    new.remove(min(new))

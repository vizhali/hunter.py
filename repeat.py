numb7=int(input())
vi1=list(map(int,input().split()[:numb7]))
count=0
vj=[]
for i in range(0,numb7+1):
   if(vi1.count(i)>1):
      vj.append(i)
if(len(vj)==0):
   print("unique")
av=sorted(vj)
print(' '.join(map(str,av)))

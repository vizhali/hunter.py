vizh=list(map(str,input()))
v=t=0
for i in range(0,len(vizh)-1):
  bob=vizh[i]
  if int(bob)!=0:
   for j in range(i+1,i+2):
    bob=bob+vizh[j]
    if int(bob)<27 and int(bob)>0: v=v+1
    elif int(bob)==0: v=v-1
    else: break
if v!=1: t=v%2
print(v+t+1)

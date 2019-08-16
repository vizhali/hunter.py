check=int(input())
zero=0
lists=list(map(int,input().split()))
news=[]
for i in range(0,check):
    if((lists.count(lists[i]))>=2):
      if lists[i] not in news:
        news.append(lists[i])
        zero=1
if(zero==0):
  print("unique")
else:
  for i in range(0,check):
    print(min(news),end=" ")
    news.remove(min(news))

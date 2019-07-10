vizh1=int(input())
bob1=input().split()
for i in range(len(bob1)):
    for j in range(i+1,len(bob1)):
        for k in range(j+1,len(bob1)):
            if(int(bob1[i])+int(bob1[j])==int(bob1[k])):
                print(bob1[i],bob1[j],bob1[k])

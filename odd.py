vizh1  =input()
bob1 = list(map(int,input().split()))
for i in range(len(bob1)):
    if (i%2 == 0 and bob1[i]%2 !=0) or (i%2!= 0 and bob1[i]%2 == 0):
        print(bob1[i],end = " ")

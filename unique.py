vizh1 = input()
bob1 = list(map(int,input().split()))
van1 = False
for i in bob1:
    if bob1.count(i) > 1:
        van1 = True
        break
print(i if van1 else "unique")

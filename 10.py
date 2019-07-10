vizh,keeri = map(int,input().split())
bob2 = list(map(int,input().split()))
bob3 = list(map(int,input().split()))
fk =1
for i in bob3:
    if i not in bob2:
        print('NO')
        fk = 0
        break
if(fk):
    print('YES')

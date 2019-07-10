bob = int(input())
man = [z for z in input().split()]
man1 = []
for i in range(len(man)):
    if man[i] == str(i):
        man1.append(man[i])
    # print(i, man[i])

if len(man1) == 0:
    print('-1')
else:
    print(' '.join(sorted(man1)))

n = int(input())
l = []
for x in range(0,n):
    k = int(input())
    l.append(k)
l.sort()
i=set(l)
secondPosition = list(i)
print((secondPosition[-2]))
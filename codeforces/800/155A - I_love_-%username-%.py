t = int(input())
l = list(map(int,input().split()))
count = 0
for _ in range(len(l)):
    max_c = l[0]
    min_c = l[0]
for i in range(len(l)):
    if max_c < l[i]:
        count +=1
        max_c = l[i]
    if min_c > l[i]:
        count +=1
        min_c = l[i]
print(count)
    
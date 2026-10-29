t = int(input())
home = []
away = []
for _ in range(t):
    x, y = map(int, input().split())
    home.append(x)
    away.append(y)

count = 0
for i in range(t):
    for j in range(t):
        if i != j and home[i] == away[j]:
            count += 1

print(count)   
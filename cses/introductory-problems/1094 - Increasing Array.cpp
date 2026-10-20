x = int(input())
y = list(map(int , input().split()))
c = 0
for i in range(1, x):
    if y[i] < y[i-1]:
        c += y[i-1] - y[i]
        y[i] = y [ i - 1]
print(c)
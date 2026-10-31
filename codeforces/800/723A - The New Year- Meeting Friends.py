z = list(map(int, input().split()))
a = sorted(z)
total = (a[1] - a[0]) + (a[2] - a[1])
print(total)
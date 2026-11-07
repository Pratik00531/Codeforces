n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
sereja = dima = 0

for turn in range(n):
    if a[l] >= a[r]:
        pick = a[l]
        l += 1
    else:
        pick = a[r]
        r -= 1

    if turn % 2 == 0:
        sereja += pick
    else:
        dima += pick

print(sereja, dima)   
t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    # Count participants who ran further than Timur (a)
    count = (b > a) + (c > a) + (d > a)
    print(count)   
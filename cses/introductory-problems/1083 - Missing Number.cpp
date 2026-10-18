def weird(n, a):
    p = set(range(1, n + 1))
    missing = list(p - set(a))
    print(*missing)

num = int(input())
a = list(map(int, input().split()))
weird(num, a)
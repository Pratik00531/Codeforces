t = int(input())

for _ in range(t):
    n = input().strip()
    result = []

    for i, digit in enumerate(n):
        if digit != '0':
            round_num = int(digit) * (10 ** (len(n) - i - 1))
            result.append(round_num)

    print(len(result))
    print(*result)
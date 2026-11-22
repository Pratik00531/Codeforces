t = int(input())
target = "codeforces"

for _ in range(t):
    s = input()
    diff_count = 0
    for i in range(10):
        if s[i] != target[i]:
            diff_count += 1
    print(diff_count)   
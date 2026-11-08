n, k = map(int, input().split())
available_time = 240 - k
solved_count = 0
time_spent = 0

for i in range(1, n + 1):
    time_spent += 5 * i
    if time_spent <= available_time:
        solved_count += 1
    else:
        break

print(solved_count)   
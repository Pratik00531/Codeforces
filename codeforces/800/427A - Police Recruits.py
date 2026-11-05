n = int(input())
recruits = 0
untreated = 0
 
# Read all events at once as a list of integers
events = list(map(int, input().split()))

for x in events:
    if x == -1:
        if recruits > 0:
            recruits -= 1
        else:
            untreated += 1
    else:
        recruits += x
 
print(untreated)

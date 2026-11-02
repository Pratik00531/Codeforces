a = input()
count = 1  
max_count = 1

for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1 

if max_count >= 7:
    print("YES")
else:
    print("NO")

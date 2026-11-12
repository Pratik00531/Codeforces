t = int(input())
for _ in range(t):
    x = input()
    y = x[:3]
    z= x[3:]
    l = sum(map(int, str(y)))
    w = sum(map(int, str(z)))
    if l == w:
        print("Yes")
    else:        
        print("No")
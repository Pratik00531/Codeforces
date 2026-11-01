a = input()
b = input()
c = input()

l = sorted(a + b)
r = sorted(c)

if l == r:
    print("YES")
else:
    print("NO")   
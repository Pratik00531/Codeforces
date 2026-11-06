n, k, l, c, d, p, nl, np = map(int, input().split())

# 1. Total toasts possible from the total drink
drink_toasts = (k * l) // nl

# 2. Total toasts possible from the limes
lime_toasts = c * d

# 3. Total toasts possible from the salt
salt_toasts = p // np

# Find the limiting factor for the group, then divide by n friends
print(min(drink_toasts, lime_toasts, salt_toasts) // n)

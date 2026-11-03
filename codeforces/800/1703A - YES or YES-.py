# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the 3-letter string
    x = input()
    
    # Convert it to lowercase and check if it equals "yes"
    if x.lower() == "yes":
        print("YES")
    else:
        print("NO")

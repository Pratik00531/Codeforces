import sys

def solve():
    # Read number of test cases
    input = sys.stdin.read
    data = input().split()
    
    iterator = iter(data)
    t = int(next(iterator))
    
    results = []
    for _ in range(t):
        n = int(next(iterator))
        # Count odd numbers in the array
        odd_count = 0
        for _ in range(n):
            val = int(next(iterator))
            if val % 2 != 0:
                odd_count += 1
        
        # If the number of odd elements is even, we can split them evenly
        # between the two colors, ensuring both color sums have the same parity.
        if odd_count % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()   
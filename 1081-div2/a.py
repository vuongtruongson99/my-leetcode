def solve():
    n = int(input())
    s = list(input())
    
    block = 0
    is_double = False
    for i in range(n):
        if s[i] != s[(i+1)%n]:
            block += 1
        else:
            is_double = True

    return block if not is_double else block + 1
    

t = int(input())
for _ in range(t):
	print(solve())

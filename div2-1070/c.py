def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    odd, even = [], []
    for i in range(n):
        if arr[i] & 1:
            odd.append(arr[i])
        else:
            even.append(arr[i])
    
    odd.sort(reverse=True)
    even.sort(reverse=True)
    
    pref = [0]
    for i in range(len(even)):
        pref.append(pref[i] + even[i])
        
    out = []
    for k in range(1, n + 1):
        temp = max(1, k - len(even))
        if temp % 2 == 0:
            temp += 1

        if temp > k or temp > len(odd):
            out.append("0")
        else:
            ans = odd[0] + pref[k - temp]
            out.append(str(ans))
    
    print(*out)

t = int(input())
for _ in range(t):
	solve()

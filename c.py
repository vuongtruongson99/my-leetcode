def solve():
	a, b = map(int, input().split())
	# a and b are odd
	if b % 2 == 1:
		if a % 2 == 1:
			return a * b + 1
		else:
			return -1
	
	b_tmp = b
	cnt = 0
	while b_tmp % 2 == 0:
		b_tmp = b_tmp // 2
		cnt += 1
	if a % 2 == 1 and cnt == 1:
		return -1

	k = 2 if a % 2 == 1 else 1
	return max(a * k + b // k, a * (b // 2) + 2)

t = int(input())
for _ in range(t):
	result = solve()
	print(int(result))

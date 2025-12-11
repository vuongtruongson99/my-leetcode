def solve():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	f = [0] * (n + 1)

	for val in a:
		if val <= n:
			f[val] += 1

	M = 0
	while M <= n and f[M] > 0:
		M += 1

	def sum_after_k1():
		sumU = 0
		u = 0
		for y in range(M):
			if f[y] == 1:
				u += 1
				sumU += y
		return sumU + (n - u) * M

	if k == 1:
		print(sum_after_k1())
		return

	p = -1
	for y in range(M):
		if f[y] >= 2:
			p = y
			break

	ans = 0
	if p != -1:
		S = p * (p - 1) // 2
		r = n - p
		if k % 2 == 0:
			ans = S + r * p
		else:
			ans = S + r * (p + 1)
	else:
		S = M * (M - 1) // 2
		r = n - M
		if r == 0:
			ans = S
		elif r == 1:
			ans = S + M
		else:
			if k % 2 == 0:
				ans = S + r * (M + 1)
			else:
				ans = S + r * M
	print(ans)

t = int(input())
for _ in range(t):
	solve()

def solve():
	n = int(input())
	b = list(map(int, input().split()))

	pos = [[] for _ in range(n + 1)]
	for i, val in enumerate(b):
		pos[val].append(i)

	ok = True
	for v in range(1, n + 1):
		if len(pos[v]) % v != 0:
			ok = False
			break

	if not ok:
		print(-1)
		return

	a = [0] * n
	label = 1
	for v in range(1, n + 1):
		m = len(pos[v])
		for i in range(0, m, v):
			for j in range(v):
				a[pos[v][i + j]] = label
			label += 1

	print(" ".join(map(str, a)))

t = int(input())
for _ in range(t):
	solve()

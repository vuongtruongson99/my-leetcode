from collections import defaultdict


read = open("cownomics.in")

n, m = map(int, read.readline().split())
spot_cows = defaultdict(set)
normal_cows = defaultdict(set)

for i in range(n):
    genes = list(read.readline().strip())
    for j, g in enumerate(genes):
        spot_cows[j].add(g)
for i in range(n):
    genes = list(read.readline().strip())
    for j, g in enumerate(genes):
        normal_cows[j].add(g)

ans = 0
for i in range(m):
    ch = spot_cows[i].intersection(normal_cows[i])
    if not len(ch):
        ans += 1

print(ans, file=open("cownomics.out", "w"))
    
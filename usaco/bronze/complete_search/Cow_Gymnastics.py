from collections import defaultdict


read = open("gymnastics.in")

k, n = map(int, read.readline().split())
ans = defaultdict(set)

arr = list(map(int, read.readline().split()))
for i in range(n):
    for j in range(i+1, n):
        ans[arr[i]].add(arr[j])

for i in range(1, k):
    arr = list(map(int, read.readline().split()))
    for j in range(n):
        s = set()
        for k in range(j+1, n):
            s.add(arr[k])
        ans[arr[j]] = ans[arr[j]].intersection(s)
print(ans)
out = 0
for k, v in ans.items():
    out += len(v)

print(out, file=open("gymnastics.out", "w"))
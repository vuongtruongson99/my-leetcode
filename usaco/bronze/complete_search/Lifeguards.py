read = open("lifeguards.in")

n = int(read.readline())
guards = []
for i in range(n):
    l, r = map(int, read.readline().split())
    guards.append((l, r))
guards.sort()

total = 0
  

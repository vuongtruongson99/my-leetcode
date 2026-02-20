read = open("triangles.in")
n = int(read.readline())
points = []

for i in range(n):
    x, y = map(int, read.readline().split())
    points.append((x, y))

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if points[i][1] == points[j][1] and points[i][0] == points[k][0]:
                area = (points[i][0] - points[j][0]) * (points[i][1] - points[k][1])
                if area < 0:
                    area *= -1
                ans = max(ans, area)
                
print(ans, file=open("triangles.out", "w"))
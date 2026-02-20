n = int(input())
arr = list(map(int, input().split()))
ans = n

for i in range(n):
    photo = [arr[i]]
    for j in range(i+1, n):
        photo.append(arr[j])
        
        if sum(photo) % len(photo):
            continue
        
        p = sum(photo) / len(photo)
        if p in photo:
            ans += 1

print(ans)
        
import sys
input = sys.stdin.readline

def solve():
    line = input().strip()
    if not line:
        return
    n = int(line)

    print(f"? 1 {n}")
    sys.stdout.flush()

    curr_sum = int(input())
    if curr_sum == -1:
        sys.exit(0)

    l, r = 1, n

    while l < r:
        target = curr_sum // 2
        split_idx = -1

        low, high = l, r - 1

        while low <= high:
            mid = low + (high - low) // 2
            print(f"? {l} {mid}")
            sys.stdout.flush()

            val = int(input())
            if val == -1:
                sys.exit(0)

            if val == target:
                split_idx = mid
                break
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1

        len_a = split_idx - l + 1
        len_b = r - split_idx

        if len_a < len_b:
            r = split_idx
            curr_sum = target
        else:
            l = split_idx + 1
            curr_sum = target

    print(f"! {curr_sum}")
    sys.stdout.flush()

        
t = int(input())
for _ in range(t):
	solve()

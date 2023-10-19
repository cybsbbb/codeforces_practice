from collections import Counter


def count():
    nums = list(map(int, input().split()))
    d = Counter(nums)
    return nums, d


def solve():
    _, d = count()
    print('- 0')
    while True:
        nums, dd = count()
        for num in dd:
            if num not in d:
                print(f'! {nums.index(num) + 1}')
                return
        flag = False
        for num in dd:
            if dd[num] > d[num]:
                flag = True
                idx = [str(i) for i, x in enumerate(nums, 1) if x != num]
                print(f'- {len(idx)} ' + ' '.join(idx))
                dd = {num: dd[num]}
                break
        if flag is False:
            print('- 0')
        d = dd


for _ in range(int(input())):
    n = int(input())
    solve()

import collections

_ = int(input())
have = list(map(int, input().split()))
_ = int(input())
problem = list(map(int, input().split()))

counter = collections.Counter(have)
# Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

for num in problem:
    print(counter[num], end=" ")

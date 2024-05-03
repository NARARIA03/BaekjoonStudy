import sys


N, K = map(int, sys.stdin.readline().split())

coin_ary = []
for _ in range(N):
    new_coin = int(sys.stdin.readline().rstrip())
    coin_ary.append(new_coin)

coin_cnt = 0
left_money = K


for i in range(len(coin_ary), 0, -1):
    coin = coin_ary[i - 1]
    # print("coin: ", coin)
    j = 0
    while left_money >= coin * (j + 1):
        j += 1
    # print(str(coin) + " count: ", j)
    coin_cnt += j
    left_money -= coin * j
    # print("left_money: ", left_money)
    if left_money == 0:
        break

print(coin_cnt)

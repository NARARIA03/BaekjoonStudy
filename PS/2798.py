_, M = map(int, input().split())
card_list = list(map(int, input().split()))

sum = 0

for i in range(0, len(card_list)):
    for j in range(i + 1, len(card_list)):
        for k in range(j + 1, len(card_list)):
            if (
                sum <= card_list[i] + card_list[j] + card_list[k]
                and card_list[i] + card_list[j] + card_list[k] <= M
            ):
                sum = card_list[i] + card_list[j] + card_list[k]
print(sum)

num = input().split()

asc_num = sorted(num) # 오름차순
desc_num = sorted(num, reverse=True) # 내림차순

if (num == asc_num):
    print('ascending')
elif (num == desc_num):
    print('descending')
else:
    print('mixed')

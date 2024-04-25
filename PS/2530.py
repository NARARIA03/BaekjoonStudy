A, B, C = map(int, input().split())
D = int(input())
start_time = A * 3600 + B * 60 + C
end_time = start_time + D

end_h = end_time // 3600
end_m = end_time % 3600 // 60
end_s = end_time % 3600 % 60

if end_h >= 24:
    end_h %= 24

print(end_h, end_m, end_s)

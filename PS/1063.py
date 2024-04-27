import sys

row_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
col_dict = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

res_row_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
res_col_dict = {7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7, 0: 8}


king, stone, N = map(str, sys.stdin.readline().split())
N = int(N)

king_y, king_x = (col_dict[int(king[1])], row_dict[king[0]])
stone_y, stone_x = (col_dict[int(stone[1])], row_dict[stone[0]])

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if len(command) == 1:
        if command == "R":
            if king_x == 7:
                continue
            elif king_y == stone_y and king_x + 1 == stone_x:
                if stone_x == 7:
                    continue
                else:
                    stone_x += 1
            king_x += 1
        elif command == "L":
            if king_x == 0:
                continue
            elif king_y == stone_y and king_x - 1 == stone_x:
                if stone_x == 0:
                    continue
                else:
                    stone_x -= 1
            king_x -= 1
        elif command == "B":
            if king_y == 7:
                continue
            elif king_x == stone_x and king_y + 1 == stone_y:
                if stone_y == 7:
                    continue
                else:
                    stone_y += 1
            king_y += 1
        elif command == "T":
            if king_y == 0:
                continue
            elif king_x == stone_x and stone_y + 1 == king_y:
                if stone_y == 0:
                    continue
                else:
                    stone_y -= 1
            king_y -= 1
    else:
        if command == "RT":
            if king_y == 0 or king_x == 7:
                continue
            elif stone_y + 1 == king_y and king_x + 1 == stone_x:
                if stone_y == 0 or stone_x == 7:
                    continue
                else:
                    stone_y -= 1
                    stone_x += 1
            king_y -= 1
            king_x += 1
        elif command == "LT":
            if king_x == 0 or king_y == 0:
                continue
            elif stone_x + 1 == king_x and stone_y + 1 == king_y:
                if stone_x == 0 or stone_y == 0:
                    continue
                else:
                    stone_x -= 1
                    stone_y -= 1
            king_x -= 1
            king_y -= 1
        elif command == "RB":
            if king_x == 7 or king_y == 7:
                continue
            elif king_x + 1 == stone_x and king_y + 1 == stone_y:
                if stone_x == 7 or stone_y == 7:
                    continue
                else:
                    stone_x += 1
                    stone_y += 1
            king_x += 1
            king_y += 1
        elif command == "LB":
            if king_x == 0 or king_y == 7:
                continue
            elif stone_x + 1 == king_x and king_y + 1 == stone_y:
                if stone_x == 0 or stone_y == 7:
                    continue
                else:
                    stone_y += 1
                    stone_x -= 1
            king_y += 1
            king_x -= 1

print(res_row_dict[king_x], end="")
print(res_col_dict[king_y])
print(res_row_dict[stone_x], end="")
print(res_col_dict[stone_y])

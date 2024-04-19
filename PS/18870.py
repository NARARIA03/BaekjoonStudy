import sys


def mapping_compress_coordinate(coordinate_set: set[int], compressed_dict: dict):
    compress_coordinate = 0
    for coordinate in coordinate_set:
        compressed_dict[coordinate] = compress_coordinate
        compress_coordinate += 1


_ = int(input())

coordinate_list = list(map(int, input().split()))
sorted_coordinate_set = sorted(set(coordinate_list))

compressed_dict = {}
mapping_compress_coordinate(sorted_coordinate_set, compressed_dict)

# print(compressed_dict)
# print("sorted list to set: ", sorted_coordinate_set)

for coordinate in coordinate_list:
    sys.stdout.write(str(compressed_dict[coordinate]) + " ")

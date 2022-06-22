# 连续输出五行*，并且每一行幸好的数量依次增加
"""
row = 1
while row <= 5:
    print("*"*row)
    row += 1

"""
from Study.class_method import Tool


def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %2d" % (col, row, col * row), end=" ")
            col += 1
        print()
        row += 1




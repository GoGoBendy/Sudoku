import random
import numpy as np
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
print(sys.getrecursionlimit())


def listchecker(obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9):
    for i in range(9):
        if (
            obj1[i] == obj2[i]
            or obj1[i] == obj3[i]
            or obj1[i] == obj4[i]
            or obj1[i] == obj5[i]
            or obj1[i] == obj6[i]
            or obj1[i] == obj7[i]
            or obj1[i] == obj8[i]
            or obj1[i] == obj9[i]
        ):
            obj1 = numchecker(obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9)
    return obj1


def numchecker(lis1, lis2, lis3, lis4, lis5, lis6, lis7, lis8, lis9):
    for i in range(9):
        if (
            lis1[i] == lis2[i]
            or lis1[i] == lis3[i]
            or lis1[i] == lis4[i]
            or lis1[i] == lis5[i]
            or lis1[i] == lis6[i]
            or lis1[i] == lis7[i]
            or lis1[i] == lis8[i]
            or lis1[i] == lis9[i]
        ):
            lis1 = random.sample(baserow, k=len(baserow))
        else:
            pass
    lis1 = listchecker(lis1, lis2, lis3, lis4, lis5, lis6, lis7, lis8, lis9)
    return lis1


baserow = [1, 2, 3, 4, 5, 6, 7, 8, 9]

row1 = random.sample(baserow, k=len(baserow))
row2 = random.sample(baserow, k=len(baserow))
row2 = numchecker(
    row2, row1, baserow, baserow, baserow, baserow, baserow, baserow, baserow
)
row3 = random.sample(baserow, k=len(baserow))
row3 = numchecker(
    row3, row1, row2, baserow, baserow, baserow, baserow, baserow, baserow
)

row4 = random.sample(baserow, k=len(baserow))
row4 = numchecker(row4, row1, row2, row3, baserow, baserow, baserow, baserow, baserow)

row5 = random.sample(baserow, k=len(baserow))
row5 = numchecker(row5, row1, row2, row3, row4, baserow, baserow, baserow, baserow)

row6 = random.sample(baserow, k=len(baserow))
row6 = numchecker(row6, row1, row2, row3, row4, row5, baserow, baserow, baserow)

row7 = random.sample(baserow, k=len(baserow))
row7 = numchecker(row7, row1, row2, row3, row4, row5, row6, baserow, baserow)

row8 = random.sample(baserow, k=len(baserow))
row8 = numchecker(row8, row1, row2, row3, row4, row5, row6, row7, baserow)


print("after")

solution = np.array([row1, row2, row3, row4, row5, row6, row7, row8])
print(solution)

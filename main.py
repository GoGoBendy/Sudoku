import random

baserow = [1, 2, 3, 4, 5, 6, 7, 8, 9]

row1 = random.sample(baserow, k=len(baserow))
print(row1)
row2 = random.sample(baserow, k=len(baserow))
print(row2)
for i in range(9):
    if row1[i] == row2[i]:
        row2 = random.sample(baserow, k=len(baserow))
row3 = random.sample(baserow, k=len(baserow))
for i in range(9):
    if row1[i] == row3[i] or row2[i] == row3[i]:
        row3 = random.sample(baserow, k=len(baserow))
row4 = random.sample(baserow, k=len(baserow))
row5 = random.sample(baserow, k=len(baserow))
row6 = random.sample(baserow, k=len(baserow))
row7 = random.sample(baserow, k=len(baserow))
row8 = random.sample(baserow, k=len(baserow))
row9 = random.sample(baserow, k=len(baserow))

print("")
print("Sudoku Puzzle")
print(f"{row1[:3]} | {row1[3:6]} | {row1[6:9]}")
print(f"{row2[:3]} | {row2[3:6]} | {row2[6:9]}")
print(f"{row3[:3]} | {row3[3:6]} | {row3[6:9]}")
print("—————————————————————————————————")
print(f"{row4[:3]} | {row4[3:6]} | {row4[6:9]}")
print(f"{row5[:3]} | {row5[3:6]} | {row5[6:9]}")
print(f"{row6[:3]} | {row6[3:6]} | {row6[6:9]}")
print("—————————————————————————————————")
print(f"{row7[:3]} | {row7[3:6]} | {row7[6:9]}")
print(f"{row8[:3]} | {row8[3:6]} | {row8[6:9]}")
print(f"{row9[:3]} | {row9[3:6]} | {row9[6:9]}")


rows = 5

# Top part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Bottom part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

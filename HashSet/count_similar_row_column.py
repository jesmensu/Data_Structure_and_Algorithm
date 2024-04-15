grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

result_map = {}
columns = {}
count = 0
for i in range(len(grid)):
    if str(grid[i]) in result_map:
        result_map[str(grid[i])] += 1
    else:
        result_map[str(grid[i])] = 1
        
for i in range(len(grid)):
    columns[i] = []
    for j in grid:
        columns[i].append(j[i])
    if str(columns[i]) in result_map:
        count += result_map[str(columns[i])]

print(count)

# ===================================================

rows = {}
columns = {}
for i in range(len(grid)):
    rows[i] = grid[i]
    columns[i] = []
    for j in grid:
        columns[i].append(j[i])
count = 0
for k1, v1 in rows.items():
    for k2, v2 in columns.items():
        if v2 == v1:
            count += 1

print(count)
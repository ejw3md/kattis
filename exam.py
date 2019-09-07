grid = []
rows, cols = [int(x) for x in input().split()]
for r in range(rows):
    grid.append(list(input()))
def shift(grid, col, group_start, group_end, apples):
    cur_idx = group_end
    for a in range(apples):
        if grid[cur_idx][col] == '#':
            print(cur_idx, apples)
        grid[cur_idx][col] = 'a'
        cur_idx-=1
    for c in range(group_start+1, cur_idx+1):
        grid[c][col] = '.'
def find_next_barrier(grid, col, start):
    idx = start
    while idx >= 0 and grid[idx][col] =='#':
        idx-=1
    return idx
def fall(grid, col):
    group_end = find_next_barrier(grid, col, len(grid)-1)
    group_start = group_end
    while group_start>0:
        apples = 0
        while group_start > 0 and grid[group_start][col] != '#':
            if grid[group_start][col] == 'a':
                apples+=1
            group_start-=1
        if group_start == 0:
            if grid[group_start][col] == 'a':
                apples+=1
                shift(grid, col, group_start-1, group_end, apples)
            else:
                shift(grid, col, group_start, group_end, apples)
            break
        shift(grid, col, group_start, group_end, apples)
        group_end = find_next_barrier(grid, col, group_start-1)
        group_start = group_end
def print_grid(grid):
    for r in grid:
        for c in r:
            print(c, end='')
        print()
for c in range(cols):
    fall(grid, c)
print_grid(grid)

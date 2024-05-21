n,m = tuple(map(int,input().split()))
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
answer=[
    [0 for _ in range(m)]
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# n:행개수, m:열개수

def in_range(x,y):
    return 0<=x<=n-1 and 0<=y<=m-1

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global order

    dxs,dys = [1,0],[0,1]

    for dx,dy in zip(dxs,dys):
        new_x,new_y = x+dx, y+dy
        if can_go(new_x,new_y):
            visited[new_x][new_y] = True
            dfs(new_x,new_y)
            
visited[0][0] = True
dfs(0,0)

print(1 if visited[n-1][m-1] else 0)
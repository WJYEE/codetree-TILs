n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dxs,dys = [1,0,-1,0],[0,1,0,-1]
output = 0
def in_range(x,y):
    return 0<=x<n and 0<=y<n
for i in range(n):
    for j in range(n):
        cnt=0
        for dx,dy in zip(dxs,dys):
            nx,ny = i+dx,j+dy
            if in_range(nx,ny) and grid[nx][ny] == 1:
                cnt+=1
        if cnt>=3 : output+=1
print(output)
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dxs,dys = [1,0,-1,0],[0,1,0,-1]
output = 0
def in_range(y,x):
    return 0<=x<n and 0<=y<n
for i in range(n):
    for j in range(n):
        cnt=0
        for dx,dy in zip(dxs,dys):
            ny,nx = j+dy,i+dx
            if in_range(nx,ny) and grid[ny][nx] == 1:
                cnt+=1
        if cnt>=3 : output+=1
print(output)
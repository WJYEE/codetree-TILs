n = int(input())
dx,dy = [-1,0,0,1],[0,-1,1,0]
x,y = 0,0
dir_num = {
    'W':0,
    'S':1,
    'N':2,
    'E':3
}
for _ in range(4):
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    x,y = x+dx[dir_num[c_dir]]*dist, y+dy[dir_num[c_dir]]*dist
print(x,y)
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
    dir_, num = map(str,input().split())
    num=int(num)
    x,y = x+dx[dir_num[dir_]]*num, y+dy[dir_num[dir_]]*num
print(x,y)
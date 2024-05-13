N = int(input())
dx,dy = [-1,0,0,1],[0,-1,1,0]
x,y = 0,0
answer = 0
cnt=0
for _ in range(N):
    dire,num = tuple(input().split())
    num = int(num)
    for _ in range(num):
        cnt+=1
        if dire == 'N':
            x,y = x+dx[2],y+dy[2]
        elif dire == 'E':
            x,y = x+dx[3],y+dy[3]
        elif dire == 'W':
            x,y = x+dx[0],y+dy[0]
        else:
            x,y = x+dx[1],y+dy[1]
        if x==0 and y==0:
            answer=1
            break
    if answer==1:
        break

if answer == 0:
    print(-1)
else : 
    print(cnt)
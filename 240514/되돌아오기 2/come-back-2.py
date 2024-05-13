x,y = 0,0
string = input()
N = len(string)
time = 0
dx,dy = [1,0,-1,0],[0,1,0,-1]
direct = 3
answer=0
for i in range(N):
    if string[i]=='L':
        direct = (direct+3)%4
    elif string[i]=='R':
        direct = (direct+1)%4
    else:
        x,y = x+dx[direct],y+dy[direct]
    time+=1
    if x==0 and y==0:
        answer=1
        break
if answer == 0:
    print(-1)
else:
    print(time)
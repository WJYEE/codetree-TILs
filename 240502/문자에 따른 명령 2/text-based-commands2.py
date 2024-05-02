x,y=0,0
order=str(input())
dx,dy = [1,0,-1,0],[0,-1,0,1]
len_order = len(order)
direct = 3
for i in range(len_order):
    if order[i] == 'L': 
        direct -=1
    elif order[i] == 'R': 
        direct +=1
    else: 
        x,y = x+dx[direct%4],y+dy[direct%4]

        
print(x,y)
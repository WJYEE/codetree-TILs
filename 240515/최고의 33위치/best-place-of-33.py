N=int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
cnt=0
m_cnt =0
for y in range(N-2):
    for x in range(N-2):
        for j in range(y,N+y):
            for i in range(x,N+x):
                cnt+=grid[j][i]
        if cnt>m_cnt:
            m_cnt=cnt
        cnt=0

print(m_cnt)
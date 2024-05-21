N,M = map(int,input().split())
# 인접리스트
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0
def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt+=1
            visited[curr_v]=True
            dfs(curr_v)

# points=[list(map(int,input().split())) for _ in range(M)]
# start_points=[]
# for i in range(len(points)):
#     start_points.append(points[i][0])
# end_points=[]
# for i in range(len(points)):
#     end_points.append(points[i][1])

# for start,end in zip(start_points,end_points):
#     graph[start].append(end)
#     graph[end].append(start)

#간선 입력 후 인접리스트에 추가 (양방향) - 위의 문단 대체체
for _ in range(m):
    x,y = tuple(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)

# 인접 행렬
graph = [
    [0 for _ in range(N+1)]
    for _ in range(N+1)
]

visited = [False for _ in range(N+1)]

def dfs(vertex):
    for curr_v in range(1,N+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
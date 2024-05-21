from collections import deque

n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# 방문할 지점들을 저장하는 queue
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and a[x][y] and not visited[x][y]

def bfs():
    visited[0][0] = True
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        # 연결체크
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

bfs()
print(1 if visited[n-1][m-1] else 0)
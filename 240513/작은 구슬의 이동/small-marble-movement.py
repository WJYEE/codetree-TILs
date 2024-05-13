n, t = map(int, input().split())
r, c, d = map(str, input().split())
x, y = int(c) - 1, int(r) - 1
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
direct = {'U': 0, 'R': 1, 'L': 2, 'D': 3}
dirnum = direct[d]

for _ in range(t):
    # 다음 위치 계산
    nx, ny = x + dx[dirnum], y + dy[dirnum]
    
    # 다음 위치가 격자 범위를 벗어나는지 확인
    if not (0 <= nx < n and 0 <= ny < n):
        t -= 1
        dirnum = 3 - dirnum
    else:
        x, y = nx, ny

print(y + 1, x + 1)
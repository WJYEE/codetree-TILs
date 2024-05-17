N,M = map(int,input().split())
answer = []

def f(curr,cnt):
    if cnt == M :  # 종료 조건
        print(*answer)
        return
    for v in range(curr, N + 1):
        answer.append(v)
        f(v + 1,cnt+1)
        answer.pop()
f(1,0)
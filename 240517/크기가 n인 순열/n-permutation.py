n = int(input())
visited = [False]*(n+1)
answer=[]
def f(curr):
    if curr == n+1:
        print(*answer)
        return
    for i in range(1,n+1):
        if visited[i] :
            continue
        visited[i] = True
        answer.append(i)
        f(curr+1)
        answer.pop()
        visited[i] = False

f(1)
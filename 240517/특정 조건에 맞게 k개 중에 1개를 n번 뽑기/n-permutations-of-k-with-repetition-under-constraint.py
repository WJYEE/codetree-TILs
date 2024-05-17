K,N = map(int,input().split())
answer=[]
def f(curr):
    if curr>=N : # 0~1 index까지 선택완료
        print(*answer)
        return
    for v in range(1,K+1):
        if answer.count(v) < 3:
            answer.append(v)
            f(curr+1)
            answer.pop()
        
f(0)
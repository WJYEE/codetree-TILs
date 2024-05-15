#입력
n,t = map(int,input().split())
upper = list(map(int,input().split()))
lower = list(map(int,input().split()))
upper.extend(lower)
for _ in range(t):
    temp = upper[2*n-1]

    for i in range(2*n-1,0,-1):
        upper[i]=upper[i-1]

    upper[0] = temp

for i in range(n):
    print(f'{upper[i]} ',end='')
print()
for i in range(n,2*n):
    print(f'{upper[i]} ',end='')
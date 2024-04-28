arr = [list(map(int,input().split())) for _ in range(2)]
r_len = len(arr) # 행 개수 = 2
c_len = len(arr[0]) # 열 개수 = 4
for i in range(r_len):
    r = sum(arr[i])/c_len
    print(f'{r:.1f}',end=' ')

print()
    
b = 0
for i in range(c_len):
    a=0
    for j in range(r_len):
        a += arr[j][i]
    b+=a
    print(f'{a//r_len:.1f}',end=' ')

print()

print(f'{b/(r_len*c_len):.1f}')
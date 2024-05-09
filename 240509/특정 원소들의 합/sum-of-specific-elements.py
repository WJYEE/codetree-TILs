arr = [list(map(int,input().split())) for _ in range(4)]
n=4
output = 0
for i in range(n):
    for j in range(i+1):
        output += arr[i][j]
print(output)
arr1 = [list(map(int,input().split())) for _ in range(3)]
garbage = map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(3)]

arr3=[
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr3[i][j] += (arr1[i][j])*(arr2[i][j])

for i in range(3):
    for j in range(3):
        print(arr3[i][j],end=' ')
    print()
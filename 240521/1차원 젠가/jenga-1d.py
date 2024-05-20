n=int(input())
block = [int(input()) for _ in range(n)]
end_of_array = n
def cut_array(start_idx,end_idx):
    global end_of_array,block
    temp=[]
    for i in range(end_of_array):
        if not(start_idx<=i<=end_idx):
            temp.append(block[i])
    end_of_array=len(temp)
    for i in range(end_of_array):
        block[i] = temp[i]
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s-1,e-1)


print(end_of_array)
for i in range(end_of_array):
    print(block[i])
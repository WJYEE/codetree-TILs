K,N = map(int,input().split())
output = []

def print_output():
    for elem in output :
        print(elem,end=' ')
    print()

def choose(curr_num):
    if curr_num == N+1:
        print_output()
        return
    for i in range(1,K+1):
        output.append(i)
        choose(curr_num+1)
        output.pop()

    return
choose(1)
'''
이코테 : 나동빈
BFS: 음료수 얼려먹기
'''


ice = []
n, m = map(int, input().split())

for _ in range(n):
    ice.append(list(map(int,input())))

def dfs(x,y):


    if (x < 0 or x >= n or y < 0 or y >= m):
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
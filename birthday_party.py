import sys

def has_bridge(connections_list):
    for i in range(len(connections_list)):
        start_v = (i+1)%len(connections_list)
        visited = [False for x in range(len(connections_list))]
        visited[i] = True
        def dfs(start_v):
            visited[start_v] = True
            for connection in connections_list[start_v]:
                if connection != i and not visited[connection]:
                    dfs(connection)
        dfs(start_v)
        if not all(visited):
            return True
    return False

while True:
    params = sys.stdin.readline().split(' ')
    n_people = int(params[0])
    connections = int(params[1])
    connections_list = [[] for z in range(n_people)]
    if n_people == connections == 0:
        break
    for i in range(connections):
        con = sys.stdin.readline().split(' ')
        a = int(con[0])
        b = int(con[1])
        connections_list[a].append(b)
        connections_list[b].append(a)
    loose = False
    for i in range(len(connections_list)):
        if len(connections_list[i]) < 2:
            loose = True
    if loose:
        print('Yes')
    else:
        loose = has_bridge(connections_list)
        if loose:
            print('Yes')
        else:
            print('No')
import sys

some_data = sys.stdin.readline().split()
home_sweet_home = int(some_data[2])
average_degree = int(some_data[1]) * 2 / int(some_data[0])
if int(some_data[3]) == home_sweet_home:
    print('leave')
elif int(some_data[0]) > 3 and int(some_data[1]) == int(some_data[0]) * (int(some_data[0]) - 1) / 2:
    print('stay')
else:
    leaving = [int(some_data[3])]
    control_list = [0] * (int(some_data[0]) + 1)
    partners_list = dict()  # dict for every cuntry with the list of partners

    for i in range(1, int(some_data[0]) + 1):
        partners_list[i] = []

    for i in range(int(some_data[1])):
        partners = sys.stdin.readline().split()
        a = int(partners[0])
        b = int(partners[1])
        control_list[a] += 1
        control_list[b] += 1
        partners_list[b].append(a)
        partners_list[a].append(b)

    neighbours_left = control_list.copy()

    def bfs(partners_list, leaving_first, sweet_home, neighbours_left, control_list):
        left = [False for x in range(len(partners_list)+1)]
        leaving_now = [False for x in range(len(partners_list)+1)]
        while leaving_first:
            leaving = leaving_first.pop()
            left[leaving] = True
            for partner in partners_list[leaving]:
                if not left[partner]:
                    neighbours_left[partner] -= 1
                    if neighbours_left[partner] <= control_list[partner]//2:
                        if partner == sweet_home:
                            print('leave')
                            exit()
                        if not leaving_now[partner]:
                            leaving_first.append(partner)
                            leaving_now[partner] = True


    bfs(partners_list, leaving, home_sweet_home, neighbours_left, control_list)
    print('stay')
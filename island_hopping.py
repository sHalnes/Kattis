import sys

n_cases = int(sys.stdin.readline())

for i in range(n_cases):
    n_islands = int(sys.stdin.readline())

    if n_islands == 0:
        print(0.000)
        sys.exit()
    islans_list = []
    for j in range(n_islands):
        coords = sys.stdin.readline().split()
        x = float(coords[0])
        y = float(coords[1])
        islans_list.append((j, x,y))

    new_islands_list = islans_list.copy()
    # preprocessing: make adj table with all distances from the first vertex
    all_dists = [sys.maxsize for _ in range(n_islands)]
    all_dists[0] = 0
    local_min_index = 0
    prev = [None for _ in range(n_islands)]

    # count the total distance of all bridges
    while islans_list:
        n, x0,y0 = islans_list.pop(local_min_index)
        local_min = sys.maxsize
        local_min_index = 0
        for x in range(len(islans_list)):
            n1, x1, y1 = islans_list[x]
            dist_x = ((x1-x0)**2 + (y1-y0)**2)**(1/2)
            if dist_x < all_dists[n1]:
                all_dists[n1] = dist_x
                prev[n1] = n
                if dist_x < local_min:
                    local_min = dist_x
                    local_min_index = x
            elif dist_x > all_dists[n1] and all_dists[n1] < local_min:
                local_min = all_dists[n1]
                local_min_index = x
    total_sum = 0
    for x in range(1,len(prev)):
        _, x0, y0 = new_islands_list[x]
        _, x1, y1 = new_islands_list[prev[x]]
        total_sum += ((x1-x0)**2 + (y1-y0)**2)**(1/2)

    if total_sum < total_sum+0.001:
       print('{:.3f}'.format(total_sum))
    else:
       print('{:.8f}'.format(total_sum))
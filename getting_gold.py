import sys

params = sys.stdin.readline().split()
width = int(params[0])
height = int(params[1])
x_p = 0
y_p = 0

maze = [[0 for x in range(width)] for y in range(height)]

for i in range(height):
    line = sys.stdin.readline()
    for j in range(width):
        maze[i][j] = line[j]
        if maze [i][j] == 'P':
            y_p = j
            x_p = i
def bfs(maze, next_step):
    gold = 0
    while next_step:
        x, y = next_step.pop()
        if maze[x][y] != '0':
            if maze[x][y] == "G":
                gold +=1
            maze[x][y] = '0'
            temp =[]
            if x > 0 and maze[x-1][y] != '#':
                if maze[x-1][y] == 'T':
                    continue
                temp.append((x-1, y))
            if x < height and maze[x+1][y] != '#':
                if maze[x+1][y] == 'T':
                    continue
                temp.append((x+1, y))
            if y > 0 and maze[x][y-1] != '#':
                if maze[x][y-1] == 'T':
                    continue
                temp.append((x, y-1))
            if y < width and maze[x][y+1] != '#':
                if maze[x][y+1] == 'T':
                    continue
                temp.append((x, y+1))
            next_step += temp

    return gold
first_step = [(x_p, y_p)]
gold = bfs(maze, first_step)
print(gold)
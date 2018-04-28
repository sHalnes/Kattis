import sys

line_1 = sys.stdin.readline().split()
concert_length = int(line_1[0])
musicians = int(line_1[1])

line_2 = sys.stdin.readline().split()
if musicians == 1:
    print(0)
    sys.exit()

weights = [int(line_2[x]) for x in xrange(len(line_2))]

# Just in case: I used this description http://www.es.ele.tue.nl/education/5MC10/Solutions/knapsack.pdf
# to construct the knapsack and to determine which element was actually taken in knapsack
# schedule = knapsack
# W = concert_length
# weights = values = breakes
def knapsack():
    schedule = [[0 for i in xrange(concert_length+1)] for j in xrange(musicians+1)]
    keep =  [[0 for i in xrange(concert_length+1)] for j in xrange(musicians+1)] # here we will add submitted 'items' aka musicians brakes
    for j in xrange(1, musicians+1):
        for w in xrange(concert_length+1):
            if weights[j-1] <= w and weights[j-1]+schedule[j-1][w-weights[j-1]] > schedule[j-1][w]:
                schedule[j][w] = weights[j-1]+schedule[j-1][w-weights[j-1]]
                keep[j][w] = 1
            else:
                schedule[j][w] = schedule[j-1][w]

    in_knapsack = []
    capacity = concert_length
    for i in xrange(musicians):
        # checking the last element in every row
        if keep[-(i+1)][capacity] == 1:
            in_knapsack.append(-(i+1))
            capacity -= weights[-(i+1)]

    return in_knapsack

in_knapsack = knapsack()

breaks_schedule_1 = breaks_schedule_2 = concert_length
time_on_scene = ['-1']*musicians

# filling in the first schedule
for muz in in_knapsack:
    break_time = weights[muz]
    time = concert_length-breaks_schedule_1
    time_on_scene[muz] = str(time)
    breaks_schedule_1 -= break_time

# filling in the second schedule
for i in xrange(len(time_on_scene)):
    if time_on_scene[i] == '-1':
        break_time = weights[i]
        time = concert_length - breaks_schedule_2
        time_on_scene[i] = str(time)
        breaks_schedule_2 -= break_time

print(' '.join(time_on_scene))
import sys


def find_dist(records):
    x_0, y_0 = records[0]
    dist = 0
    for i in range(1, len(records)):
        x_1, y_1 = records[i]
        dist += ((x_0 - x_1)**2 + (y_0 - y_1)**2)**(1/2)
        x_0, y_0 = x_1, y_1
    return dist

n_t = sys.stdin.readline().split()
n = int(n_t[0])
t = float(n_t[1])

actual_run = []
GPS_record = []

t_prev = 0
t_gps = 0
# read the coords and timestamp
for i in range(n):
    data = sys.stdin.readline().split()
    # record coords in actual run list and find GPS coords after t sec
    x = float(data[0])
    y = float(data[1])
    t_run = int(data[2])

    actual_run.append((x,y))
    x_0, y_0 = actual_run[i-1]
    if i == 0:
        continue
    while t_gps <= t_run:
        t_ratio = (t_gps - t_prev)/(t_run - t_prev)
        x_gps = x_0 + t_ratio*(x - x_0)
        y_gps = y_0 + t_ratio*(y - y_0)
        GPS_record.append((x_gps, y_gps))
        t_gps += t
    t_prev = t_run
if GPS_record[-1] != actual_run[-1]:
    GPS_record.append(actual_run[-1])

dist_actual = find_dist(actual_run)
dist_GPS = find_dist(GPS_record)
difference = abs(dist_actual - dist_GPS)
print((difference/dist_actual)*100)
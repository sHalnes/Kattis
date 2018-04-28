import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()

all_trains = [0] * n
for i in xrange(n):
    car = int(sys.stdin.readline())
    all_trains[-(i + 1)] = car
    # all_trains.append(car)


def LIS(sequence):
    if len(sequence) == 0:
        return 0
    else:
        LIS_sequence = [1] * len(sequence)
        for i in xrange(1, len(sequence)):
            for j in xrange(0, i):
                if sequence[i] > sequence[j]:
                    LIS_sequence[i] = max(LIS_sequence[j] + 1, LIS_sequence[i])
        return LIS_sequence


goint_up = LIS(all_trains)

trains_down = [i * (-1) for i in all_trains]
going_down = LIS(trains_down)
total_length = []
for i in xrange(len(going_down)):
    total_length.append(goint_up[i] + going_down[i] - 1)

print max(total_length)
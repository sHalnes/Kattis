import sys

villagers = int(sys.stdin.readline())
evenings = int(sys.stdin.readline())
song_list = dict()
all_songs = 0
# fill in dict
for villager in range(1, villagers + 1):
    song_list[villager] = set()

for eve in range(evenings):
    present = (sys.stdin.readline()).split()
    present = [int(x) for x in present]
    del present[0]
    bard = False
    song_set = set()
    if 1 in present:
        bard = True
        all_songs += 1
    for person in present:
        if bard and person in song_list:
            song_list[person].add(eve)
        if not bard:
            song_set = song_set.union(song_list[person])
    if not bard:
        for person in present:
            song_list[person] = song_list[person].union(song_set)

know_all = []
for person in song_list:
    if len(song_list[person]) == all_songs:
        know_all.append(person)
know_all.sort()
for e in know_all:
    print(e)

'''
in 

4
3
2 1 2
3 2 3 4
3 4 2 1

out
1
2
4



in

8
5
4 1 3 5 6
2 5 6
3 6 7 8
2 6 2
4 2 6 8 1

out
1
2
6
8

in

5
3
2 1 3
2 2 1
4 2 1 4 5

out
1

'''
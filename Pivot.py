import sys
n_elements = int(sys.stdin.readline())
data = sys.stdin.readline().split()
n = []
for i in data:
    n.append(int(i))
pivot_candidat = [n[0]]
maxi = n[0]
for i in range(1,len(n)):
    if n[i] > maxi:
        pivot_candidat.append(n[i])
    while True:
        if pivot_candidat and pivot_candidat[-1] > n[i]:
            pivot_candidat.pop()
        else:
            break
    maxi = max(n[i], maxi)
print(len(pivot_candidat))
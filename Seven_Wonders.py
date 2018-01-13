import sys

s = sys.stdin.readline()
s_wonders = dict()
for i in s:
    if i in s_wonders:
        s_wonders[i] += 1
    elif i != '\n':
        s_wonders[i] = 1

# mult_factor = 0
# if len(s_wonders) == 3:
#     mult_factor = sys.maxsize
#     for key in s_wonders:
#         if s_wonders[key] < mult_factor:
#             mult_factor = s_wonders[key]
# summen = 7*mult_factor

summen = 0
mult_factor = 0
triples = False
if len(s_wonders) == 3:
    mult_factor = sys.maxsize
    triples = True

for key in s_wonders:
    summen += (s_wonders[key]**2)
    if triples and mult_factor > s_wonders[key]:
        mult_factor = s_wonders[key]
print(summen + mult_factor * 7)


# TCGTTC = 21
# CCC = 9
# TTCCGG = 26


'''for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])
# Solve the test case and output the answer'''
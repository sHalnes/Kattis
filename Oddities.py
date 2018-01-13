import sys

n = int(sys.stdin.readline())
for i in range(n):
    tall = int(sys.stdin.readline())
    if tall%2 > 0:
        print(tall, 'is odd')
    else:
        print(tall, 'is even')





'''
simple input

3
10
9
-5


simple output
10 is even
9 is odd
-5 is odd
'''

'''for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])
# Solve the test case and output the answer'''
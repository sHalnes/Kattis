import sys

def flip(n, binary_heap):
    if binary_heap[n] == 0:
        changes = 1
        binary_heap[n] = 1
    else:
        binary_heap[n] = 0
        changes = -1
    # update all sums
    while n > 0:
        n = (n-1)//2
        binary_heap[n] += changes


def count(right, left, binary_heap):
    sum_correction_left = 0
    sum_correction_right = 0
    while left != right:
        # left side
        root = (left-1)//2
        if left%2 != 0:
            sum_correction_left +=binary_heap[root] - binary_heap[left]
        left = root
        # right side
        root = (right-1)//2
        if right%2 == 0:
            sum_correction_right += binary_heap[root] - binary_heap[right]
        right = root
    n_bits = binary_heap[left] - sum_correction_right - sum_correction_left
    print(n_bits)

B_Q = sys.stdin.readline().split() # bits and queries
n_bits = int(B_Q[0])
n_queries = int(B_Q[1])

# # making binary heap
array_size = 0
current_level = 0
counter = 0
while current_level < n_bits:
    current_level = 2**counter
    array_size += current_level
    counter += 1
offset = array_size - current_level

binary_heap = [0 for x in range(array_size)]


for _ in xrange(n_queries):
    query = sys.stdin.readline().split()
    if query[0] == 'F':
        n = int(query[1])
        flip(n+offset, binary_heap)
    else:
        right = int(query[1]) + offset
        left = int(query[2]) + offset
        count(right, left, binary_heap)
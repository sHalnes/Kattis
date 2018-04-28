import sys

n_cases = int(sys.stdin.readline())
arr = []
position = [0 for i in xrange(n_cases+1)]

# read all elements to array and filling in positional array O(n)
for pos in xrange(1,n_cases+1):
    tall = int(sys.stdin.readline())
    arr.append(tall)
    position[tall] = pos

if n_cases == 1:
    print(0)
    sys.exit()

# making binary heap
array_size = 0
current_level = 0
counter = 0
while current_level < n_cases:
    current_level = 2**counter
    array_size += current_level
    counter += 1
offset = array_size - current_level

binary_heap = [0 for x in xrange(array_size)]

for i in xrange(offset, offset+n_cases):
    binary_heap[i] = 1


def count(right, left):
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



def update(n):
    if binary_heap[n] == 0:
        changes = -1
    else:
        changes = 1
    while n > 0:
        n = (n-1)//2
        binary_heap[n] += changes

idx = 0
while idx < n_cases:
    update(idx+offset)
    idx += 1

index_start = 1
index_end = n_cases

while index_start <= index_end:
    binary_heap[position[index_start]+offset-1] = 0
    update(position[index_start]+offset-1)
    count(offset, position[index_start]+offset-1)
    if index_start != index_end:
        binary_heap[position[index_end] + offset-1] = 0
        update(position[index_end] + offset-1)
        count(position[index_end]+offset-1, len(binary_heap)-1)
    index_start += 1
    index_end -= 1

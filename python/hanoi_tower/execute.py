# algorithm: hanoi tower

# input: height of tower
# output: steps to move all disks from A to C

# 1. move n-1 disks from A to B
# 2. move nth disk from A to C
# 3. move back n-1 disks from B to A
# 4. loop 1-3 until all disks are moved

def hanoi_tower(height, a = 'A', b = 'B', c = 'C'):
    if height == 1:
        print(a, '=>', c)
        return

    hanoi_tower(height - 1, a, c, b)
    print(a, '=>', c)
    hanoi_tower(height - 1, b, a, c)

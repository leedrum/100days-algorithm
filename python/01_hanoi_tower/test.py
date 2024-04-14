import execute as ex

print('-------- height = 1 --------')
ex.hanoi_tower(1)

print('-------- height = 2 --------')
ex.hanoi_tower(2)

print('-------- height = 3 --------')
ex.hanoi_tower(3)

### OUTPUT ###

# -------- height = 1 --------
# A => C
# -------- height = 2 --------
# A => B
# A => C
# B => C
# -------- height = 3 --------
# A => C
# A => B
# C => B
# A => C
# B => A
# B => C

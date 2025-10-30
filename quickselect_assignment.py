import random

def quickselect(A, i):
    # i is 1-based: 1 = smallest
    if len(A) == 1:
        return A[0]

    pivot = random.choice(A)
    lows = [x for x in A if x < pivot]
    highs = [x for x in A if x > pivot]
    pivots = [x for x in A if x == pivot]

    if i <= len(lows):
        return quickselect(lows, i)
    elif i <= len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, i - len(lows) - len(pivots))

# --- test 1: small mixed list ---
A1 = [9, 1, 5, 3, 7, 4, 8, 2, 6]
print("1st:", quickselect(A1, 1))   # expect 1
print("5th:", quickselect(A1, 5))   # expect 5
print("9th:", quickselect(A1, 9))   # expect 9

# --- test 2: already sorted ---
A2 = list(range(1, 21))
print("sorted, 10th:", quickselect(A2, 10))  # expect 10

# --- test 3: random bigger list ---
A3 = list(range(1, 101))
random.shuffle(A3)
print("random 100, 25th:", quickselect(A3, 25))  # should be 25

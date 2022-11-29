import numpy as np

PERC = 256

np.set_printoptions(precision=PERC)

# take input for number n
want = int(input("How many heads in a row? "))


from decimal import *
getcontext().prec = PERC

# flips approximation is floor ln(4)*2^want
flips = int(np.floor(np.log(4) * 2**want))

p = 0.5

DATATYPE = np.dtype(Decimal)

a = np.zeros((want + 1, want + 1), dtype=DATATYPE)
a.fill(Decimal(0.0))
for i in range(want):
    a[i, 0] = Decimal(1 - p)
    a[i, i + 1] = Decimal(p)
a[want, want] = Decimal(1.0)

#     0
dp = [None,np.copy(a)]

for i in range(2,1000):
    if 2**i <= (flips * 3): # more better than less
        dp.append(np.matmul(dp[-1],dp[-1]))
    if i % 5 == 0:
        print("DP Table generated to",i)

print(dp)

def heads_in_a_row(flips, p, want):
    needed = flips
    final = np.zeros((want + 1, want + 1), dtype=DATATYPE)
    for i in range(len(dp),0,-1):
        while needed >= 2**i:
            needed -= 2**i
            final = np.matmul(final, dp[i], dtype=DATATYPE)
    # np.linalg.matrix_power(a, flips,)
    return final[0, want]

import time
t = time.time()
probability = heads_in_a_row(flips=flips, p= 0.5, want=want)
print("Took",time.time() -t , "seconds")

print(f"Initial: {flips}: {probability}")
if probability < 0.5:
    print("Increasing!")
    while (probability) < 0.5:
        flips += 1
        probability = heads_in_a_row(flips=flips, p= 0.5, want=want)
        if flips % 5 == 0:
            print(f"Proc: {flips}: {probability}")
elif probability > 0.5:
    print("Decreasing!")
    while (probability) > 0.5:
        flips -= 1
        probability = heads_in_a_row(flips=flips, p= 0.5, want=want)
        if flips % 5 == 0:
            print(f"Proc: {flips}: {probability}")
print(f"End: {flips}: {probability}")
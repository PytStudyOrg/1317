import random import shuffle

N = int(input())

A = [ randint(1,N) for x in range(N) ]

shuffle(A)

print(A)


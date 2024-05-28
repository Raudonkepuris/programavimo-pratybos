#UZD 1
fib_sqc = [0 ,1]

for i in range(2, 20):
    fib_sqc.append(fib_sqc[i-2] + fib_sqc[i-1])

print("Fibonacio sekos pirmieji 20 nariu: ")
for i in fib_sqc:
    print(i, end=" ")
print("\n")


#UZD 2
pi_10 = 3
pask_sk = 2
for i in range(1, 11):
    if i % 2 != 0:
        pi_10 += 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    else:
        pi_10 -= 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    pask_sk = pask_sk + 2

print(pi_10)

pi_100 = 3
pask_sk = 2
for i in range(1, 101):
    if i % 2 != 0:
        pi_100 += 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    else:
        pi_100 -= 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    pask_sk = pask_sk + 2

print(pi_100)

pi_10000 = 3
pask_sk = 2
for i in range(1, 10001):
    if i % 2 != 0:
        pi_10000 += 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    else:
        pi_10000 -= 4 / (pask_sk * (pask_sk + 1) * (pask_sk + 2))
    pask_sk = pask_sk + 2

print(pi_10000)

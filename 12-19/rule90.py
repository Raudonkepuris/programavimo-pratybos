import matplotlib.pyplot as plt

# initial = "0100101000000001000000100001000000000001000000010100"
initial = "0000000000000000000000000100000000000000000000000000"
initial = [int(i) for i in str(initial)]

patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
result = [0, 1, 0, 1, 1, 0, 1, 0]

gens = [initial]

for j in range(0, 60):
    new = []
    for i, state in enumerate(initial):
        i0 = i-1
        i1 = i+1
        if i1 == len(initial):
            i1 = 0
        # print(i0, i, i1)
        pattern = [str(initial[i0]), str(initial[i]), str(initial[i1])]
        pattern = ''.join(pattern)

        # print(pattern)

        new.append(result[patterns.index(pattern)])

    initial = new
    gens.append(new)
    # print(initial)

plt.ylim(0, len(gens))

for y, gen in enumerate(gens):
    for x, state in enumerate(gen):
        if state == 0:
            plt.scatter(x, y, marker='s', c="#000000")
        else:
            plt.scatter(x, y, marker='s', c="#FFFFFF")
    plt.pause(0.0001)


plt.show()
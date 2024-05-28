import sys

# 7 užduotis
print("\n=== 7 užduotis ===\n")

argumentai = sys.argv[1:]
print(f"Pateikti argumentai {', '.join(argumentai)}")

# 8 užduotis
print("\n=== 8 užduotis ===\n")

arg_skaicius = len(sys.argv[1:])
pirminis = True
nulis = False

if arg_skaicius == 1:
    pirminis = False
elif arg_skaicius == 0:
    nulis = True
    pirminis = False
else:
    for i in range(2, int(arg_skaicius/2)+1):
        if arg_skaicius % i == 0:
            pirminis = False
            break

if nulis and not(pirminis):
    print("Argumentu nebuvo pateikta")
elif pirminis:
    print(f"Skaicius {arg_skaicius} yra pirminis")
else:
    print(f"Skaicius {arg_skaicius} nera pirminis")

if "-" not in sys.argv[1:]:
    # 9 užduotis
    print("\n=== 9 užduotis ===\n")

    pirminiai = []
    sudetiniai = []

    int_arg = [int(i) for i in sys.argv[1:]]
    for i in int_arg:
        pirminis = True
        nulis = False
        vienas = False

        if i == 1:
            pirminis = False
            vienas = True
        elif i == 0:
            nulis = True
            pirminis = False
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    pirminis = False
                    break

        if nulis and not(pirminis):
            print("Duotas 0")
        elif pirminis:
            pirminiai.append(str(i))
        elif not(pirminis) and not(vienas):
            sudetiniai.append(str(i))

    print(f"Pateikti pirminiai skaiciai: {', '.join(pirminiai)}")
    print(f"Pateikti sudetiniai skaiciai: {', '.join(sudetiniai)}")
else:
    # 10 užduotis
    print("\n=== 10 užduotis ===\n")
    pirminiai = []

    bruksn_ind = sys.argv.index("-")

    int_arg = range(int(sys.argv[bruksn_ind-1]), int(sys.argv[bruksn_ind+1])+1)
    for i in int_arg:
        pirminis = True
        nulis = False

        if i == 1:
            pirminis = False
        elif i == 0:
            nulis = True
            pirminis = False
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    pirminis = False
                    break

        if nulis and not(pirminis):
            print("Duotas 0")
        elif pirminis:
            pirminiai.append(str(i))

    print(f"Pateikti pirminiai skaiciai: {', '.join(pirminiai)}")
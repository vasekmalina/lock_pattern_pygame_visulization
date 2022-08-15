import itertools
import  pathlib
path = pathlib.Path(__file__).parent.resolve()

a = ["02", "06", "08", "17", "20", "26", "28", "35", "53", "60", "62", "68", "71", "80", "82", "86"]
b = ["1", "3", "4", "4", "1", "4", "5", "4", "4", "3", "4", "7", "4", "4", "5", "7"]

variations = []

for i in range(4,10):
    perms = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8], i))
    iternum = []

    for var in perms:
        s = ""
        for num in var:
            s += str(num)
        
        possible = True
        for x, y in zip(a,b):
            if x in s and y not in s:
                possible = False
            if x in s and y in s:
                ai = s.index(x)
                bi = s.index(y)
                if bi > ai:
                    possible = False
                    break

        if possible:
            variations.append(s)
            iternum.append(s)

    print(i, "dots combinations: ", len(iternum))

print("There are:", len(variations), "combinations in total.")



with open(str(path) + "//combinations.txt", "a") as f:
    for item in variations:
        f.write(item + "\n")

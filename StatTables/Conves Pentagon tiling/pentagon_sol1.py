sides = [[], [], [], [], []]
angles = [[], [], [], [], []]
B = []
C = []
results = ""

data = open("pent_sol1.csv", "w")
data.write("A, B, C, D, E\n")

for i in range(180):
    B.append(i)
    C.append(180-i)


for j in range(360):
    for k in range(0, 359-j):
        angles[0].append(j)
        angles[3].append(k)
        angles[4].append(360-k)

for l in range(100):
    for m in range(len(angles)):
        results += str(angles[m][l]) + ","
    results = results[:-1]
    data.write(results + "\n")
    results = ""
data.close()



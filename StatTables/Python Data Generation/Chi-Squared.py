import csv

data = open("Chi-Squared_Dist.csv", "w")
data.write("k, x, p\n")

with open('Book1.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    file_list = list(reader)
    del file_list[0]


for row in file_list:
    del row[-1]

p = file_list[0]
del file_list[0]
p = p[1:]
k = []


for item in file_list:
    k.append(item[0])
    del item[0]

print p
print file_list

print len(p)
print len(file_list)
for i in range(len(file_list)):
    for l in range(len(p)):
        result = str(k[i]) + "," + str(file_list[i][l]) + "," + str(p[l])
        data.write(result + "\n")


import csv

data = open("pent_type.csv", "w")
data.write("Sol #,Type\n")

with open('pent.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    file_list = list(reader)
    del file_list[0]

i=0
for item in file_list:
    if item[1] + item[2] == 180 and item[0] + item[3] + item[4] == 360:
        data.write(str(i) + ",1\n")
        i += 1

    elif item[7] == item[9] and item[1]+item[3] == 180:
        data.write(str(i) + ",2\n")
        i += 1
    elif item[5] == item[6] and item[8] == item[7]+item[9] and all((item[0],item[2],item[3])) == 120:
        data.write(str(i) + ",3\n")
        i += 1
    else:
        data.write(str(i) + ",None\n")
        i += 1



import numpy as np
# Load file

data_file = open("pentagon_data.csv", 'r')
data = data_file.readlines()
data_file.close()

training_file = open("pentagon_train_data.csv", 'w')

test_file = open("pentagon_test_data.csv", 'w')

# Look at all entries of each type at a time
for i in range(1, len(data)):
    # Ignore side data
    vals = data[i].split(',')
    vals = ','.join(vals[:4])

    output = str((i//100)+1)+','+vals+'\n'
    #Set aside 80 entries for training, 20 for testing
    if i % 100 <= 80 and i//100+1 < 16:
        training_file.write(output)
    elif i//100+1 < 16:
        test_file.write(output)

training_file.close()
test_file.close()
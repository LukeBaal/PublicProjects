#!/usr/bin/python
import scipy.stats as st

file = open("TScoreDist.csv", "w")

ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,40,60,120,1000]
tail = [0.4,0.25,0.1,0.05,0.025,0.01,0.005,0.001,0.0005]
file.write("n, t, prob\n")
for n in ls:
    for item in tail:
        file.write(str(n) + ", " + str(item) + ", " + str(st.t.ppf(item,n))+"\n")


file.close()

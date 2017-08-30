#!/usr/bin/python
import scipy.stats as st

file = open("NormalDist.csv", "w")

i = -3.6
while(i<=3.6):
    x = st.norm.cdf(i)
    file.write(str(i) + ", " + str(x) + "\n")
    i += 0.01

file.close()

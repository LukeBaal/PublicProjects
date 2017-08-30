import math

def bin_dist(n,r,pi):
    nCr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return nCr*(pi**r)*(1-pi)**(n-r)

pi=[0.01]

x = 0.05
while x<=0.50:
    pi.append(x)
    x += 0.05

file = open("BinDist.csv", "w")
file.write("n, x, pi, p\n")

for i in range(1,21):
    for j in range(0,i+1):
        for k in pi:
            file.write(str(i) + ", " + str(j) + "," + str(k) + ", " +  str(bin_dist(i,j,k))+"\n")

import time


class Counter(object):  # Counter class to keep track of solution count and time elapsed
    def __init__(self):
        self.count = 0

    def increment(self):  # Increment count variable
        self.count += 1

    def get_count(self):  # Return count variable
        return self.count


def print_sol(ls, n):
    print_list = ['']
    for x in range(0, n):
        print_list[0] += " _"

    for i in range(1, len(ls)+1):
        print_list.append('')
        for j in range(0, n):
            if j+1 == int(ls[i-1]):
                print_list[i] += '|Q'
            else:
                print_list[i] += '|_'
        print_list[i] += '|'

    for row in print_list:
        print row


def n_queen(u, n, s=""):
    if len(u) is 0:  # Base case: One possible solution formed, check if it works
        success = False
        for j in range(0, n):  # Nested Loop to compare each pair of queens
            for k in range(0, n):
                if j != k:  # Avoid comparison of a queen with itself
                    if abs(int(s[j])-int(s[k])) != (0 or (abs(j-k))):  # True if pair of queens are not in conflict
                        success = True
                    else:
                        success = False
                        break  # If pair of queens are in conflict break second loop
            else:
                continue  # If pair of queens are NOT in conflict, continue first loop
            break  # If pair of queens are in conflict break first loop

        if success:  # If bool variable is True after each comparison, then the solution holds
            sol_counter.increment()
            print_sol(list(s), n)
            print "Solution #:", sol_counter.get_count()
            # print "Success!", list(s), "Solution #:", sol_counter.get_count()
    else:
        for i in range(0, len(u)):
            n_queen(u[:i] + u[i+1:], n, s + u[i])  # Recursive step to generate all possible combinations


sol_counter = Counter()
start = time.time()
n_queen("12345", 5)  # Call function to find solutions (Should be 10 total solutions)
end = time.time()
print "Total time elapsed for 5x5 board w/ 5 queens: ", end - start
print "------------------------------------------------------------"

sol_counter = Counter()
start = time.time()
n_queen("123456", 6)  # Call function to find solutions (Should be 4 total solutions)
end = time.time()
print "Total time elapsed for 6x6 board w/ 6 queens: ", end - start
print "------------------------------------------------------------"

sol_counter = Counter()
start = time.time()
n_queen("12345678", 8)  # Call function to find solutions (Should be 92 total solutions)
end = time.time()
print "Total time elapsed for 8x8 board w/ 8 queens: ", end - start
print "------------------------------------------------------------"


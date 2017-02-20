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


def n_queen(n):
    queens = [1, 2, 3, 4, 5, 6, 7, 8]
    used = []

    for a in queens:
        queens.remove(a)
        for b in queens:
            queens.remove(b)
            for c in queens:
                queens.remove(c)
                for d in queens:
                    queens.remove(d)
                    for e in queens:
                        queens.remove(e)
                        for f in queens:
                            queens.remove(f)
                            for g in queens:
                                if n == 8:
                                    queens.remove(g)
                                    used.append(a)
                                    used.append(b)
                                    used.append(c)
                                    used.append(d)
                                    used.append(e)
                                    used.append(f)
                                    used.append(g)
                                    used.append(queens[0])

                                    # Go if solution works
                                    success = False
                                    for j in range(0, n):  # Nested Loop to compare each pair of queens
                                        for k in range(0, n):
                                            if j != k:  # Avoid comparison of a queen with itself
                                                # True if pair of queens are not in conflict
                                                if abs(int(used[j]) - int(used[k])) != (0 or (abs(j - k))):
                                                    success = True
                                                else:
                                                    success = False
                                                    break  # If pair of queens are in conflict break second loop
                                        else:
                                            continue  # If pair of queens are NOT in conflict, continue first loop
                                        break  # If pair of queens are in conflict break first loop

                                    if success:  # If still true after each comparison, then the solution holds
                                        sol_counter.increment()
                                        print_sol(used, n)
                                        print "Solution #:", sol_counter.get_count()

                                # Reset queens and used arrays
                                used = []
                                queens.append(g)
                                queens.sort()
                            queens.append(f)
                            queens.sort()
                        queens.append(e)
                        queens.sort()
                    queens.append(d)
                    queens.sort()
                queens.append(c)
                queens.sort()
            queens.append(b)
            queens.sort()
        queens.append(a)
        queens.sort()

start = time.time()
sol_counter = Counter()
n_queen(8)
end = time.time()
print "Time elapsed: ", end - start

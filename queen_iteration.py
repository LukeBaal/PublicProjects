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
		used.append(a)
		
		for b in queens:
			queens.remove(b)
			used.append(b)
			
			for c in queens:
				queens.remove(c)
				used.append(c)
				
				for d in queens:
					queens.remove(d)
					used.append(d)
					
					for e in queens:
						queens.remove(e)
						used.append(e)
						
						for f in queens:
							queens.remove(f)
							used.append(f)
							
							for g in queens:
								queens.remove(g)
								used.append(g)
								
								print used
								queens.insert(int(g)-1,g)
							
							queens.insert(int(f)-1,f)
						
						queens.insert(int(e)-1,e)
					
					queens.insert(int(d)-1,d)
				
				queens.insert(int(c)-1,c)
				
			queens.insert(int(b)-1,b)
		
		queens.insert(int(a)-1,a)

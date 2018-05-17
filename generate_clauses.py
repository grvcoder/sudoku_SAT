n = 3
number_of_clauses = 0
number_of_literals = 0
clauses = []
#Generate clauses to make sure that there is at least one number in each place
def atleast_one():
    global number_of_clauses
    global number_of_literals
    clause = ""
    for rows in range(1, n+1):
        for cols in range(1, n+1):
            for value in range(1, n+1):
                clause += str(rows)+str(cols)+str(value)+" "
            clause+=str(0)
            number_of_literals+=n
            clauses.append(clause)
            clause=""
            number_of_clauses+=1

def no_repeat_rows():
    global number_of_clauses
    global number_of_literals
    clause = ""
    for rows in range(1, n+1):
        for value in range(1, n+1):
            for x in range(1, n):
                for y in range(x+1, n+1):
                    clause += "-"+str(rows)+str(x)+str(value)+" "+"-"+str(rows)+str(y)+str(value)+" "+str(0)
                    number_of_literals+=2
                    clauses.append(clause)
                    number_of_clauses+=1
                    clause = ""

def no_repeat_cols():
    global number_of_clauses
    global number_of_literals
    clause = ""
    for cols in range(1, n+1):
        for value in range(1, n+1):
            for x in range(1, n):
                for y in range(x+1, n+1):
                    clause += "-"+str(x)+str(cols)+str(value)+" "+"-"+str(y)+str(cols)+str(value)+" "+str(0)
                    number_of_literals+=2
                    clauses.append(clause)
                    number_of_clauses+=1
                    clause = ""

def main():
    atleast_one()
    no_repeat_rows()
    no_repeat_cols()
    print "p" + " cnf"+" "+str(27)+" "+str(number_of_clauses)
    for clause in clauses:
        print clause
main()

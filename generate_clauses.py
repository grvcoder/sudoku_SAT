n = 9 #Number of rows/columns
number_of_clauses = 0 #Total number of clauses
number_of_literals = 0 #Total number of literals
clauses = [] #List to maintain all the clauses

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

#Generate clauses to make sure that no number is repeated in a row
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

#generate clauses to make sure that no number is repeated in a column
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


#generate clauses to make sure that no number repeats in a 3x3 block
def no_repeat_blocks():
    global number_of_clauses
    global number_of_literals
    clause = ""
    for value in range (1, 10):
        for x in range(0,3):
            for y in range(0,3):
                for row in range(3*x+1, 3*x+4):
                    for col in range(3*y+1, 3*y+4):
                        for i in range(3*x+1, 3*x+4):
                            for j in range(3*y+1, 3*y+4):
                                if (i==row and j==col):
                                    continue
                                clause += "-"+str(row)+str(col)+str(value)+" -"+str(i)+str(j)+str(value)+" "+str(0)
				number_of_literals+=2
                                number_of_clauses+=1
                                clauses.append(clause)
				clause = ""

def main():
    atleast_one()
    no_repeat_rows()
    no_repeat_cols()
    no_repeat_blocks()
    print "p" + " cnf"+" "+str(n)+str(n)+str(n)+" "+str(number_of_clauses)
    for clause in clauses:
        print clause


main()
no_repeat_blocks()

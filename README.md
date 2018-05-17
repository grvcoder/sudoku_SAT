# sudoku_SAT

This code provides a valid solution to a sudoku using a SAT solver

Following are the scripts used:
generate_clauses.py : This script generates the clauses in DIMACS format, to be accepted by the SAT sover
clauses.txt : will contain the output generated by the generate_clauses.py script
sol.out : will contain the output of the SAT solver (miniSat in my case)

Run:

python generate_clauses.py > clauses.txt

minisat clauses.txt sol.out



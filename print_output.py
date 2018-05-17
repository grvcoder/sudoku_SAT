import sys
def main():
    n = 3
    row_count=n;
    
    file = open(sys.argv[1], "r")
    file.readline()
    row = ""
    lines = file.readlines()
    words = lines[0].split()
    for word in words:
        if int(word) > 0:
            w = int(word)%10
            row += str(w)+" "
            row_count -= 1
            if row_count==0:
                print row
                row = ""
                row_count = n

main()

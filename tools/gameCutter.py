import sys

def isNumber(nb):
    try:
        int(nb)
    except:
        sys.stderr.write("Error: '" + str(nb) + "' is not a number\n")
        exit(84)

def doStuff(file, newfile, start, end):
    newfile = open(newfile, "w")
    for i in range(0, end):
        line = file.readline()
        if i > start:
            newfile.write(line)
    file.close()
    newfile.close()

if __name__ == "__main__":
    if "-h" in sys.argv:
        print("USAGE\n\t./mytool file newfile")
        print("DESCRIPTION\t")
        print("\tfile\tfile to copy containing the games")
        print("\tnewfile\tname of the new file")
        print("\tstart\tthe start line of the copy")
        print("\tend\tthe end line of the copy")
        exit(0)
    elif len(sys.argv) != 5:
        sys.stderr.write("Bad arguments: \"./mytool file newfile start end\"\n")
        exit(84)
    elif sys.argv[1] == sys.argv[2]:
        sys.stderr.write("Please choose a different filename\n")
        exit(84)
    isNumber(sys.argv[3])
    isNumber(sys.argv[4])
    if int(sys.argv[3]) > int(sys.argv[4]):
        sys.stderr.write("start line must be inferior to end line\n")
        exit(84)
    try:
        file = open(sys.argv[1], "r")
    except:
        sys.stderr.write("No such file : " + sys.argv[1] + "\n")
        exit(84)
    doStuff(file, sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    exit(0)
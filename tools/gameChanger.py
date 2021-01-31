import sys

def isNumber(nb):
    try:
        int(nb)
    except:
        sys.stderr.write("Error: '" + str(nb) + "' is not a number\n")
        exit(84)

def doStuff(file, newfile, nb):
    newfile = open(newfile, "w")
    for line in file.readlines():
        line = line.split(':')
        newfile.write(str(nb) + ':' + line[1] + ':' + line[2])
        nb -= 1
    file.close()
    newfile.close()

# def custom(file, newfile, nb):
#     newfile = open(newfile, "w+")
#     for line in file.readlines():
#         if nb < 2000001 and nb > 1000000:
#             newfile.write(line)
#         nb -= 1
#     file.close()
#     newfile.close()

if __name__ == "__main__":
    if "-h" in sys.argv:
        print("USAGE\n\t./mytool file newfile")
        print("DESCRIPTION\t")
        print("\tfile\tfile to copy containing the games")
        print("\tnewfile\tname of the new file")
        print("\tnb\tnumber of lines you want to copy to the new file")
        exit(0)
    elif len(sys.argv) != 4:
        sys.stderr.write("Bad arguments: \"./mytool file newfile nb\"\n")
        exit(84)
    elif sys.argv[1] == sys.argv[2]:
        sys.stderr.write("Please choose a different filename\n")
        exit(84)
    isNumber(sys.argv[3])
    try:
        file = open(sys.argv[1], "r")
    except:
        sys.stderr.write("No such file : " + sys.argv[1] + "\n")
        exit(84)
    doStuff(file, sys.argv[2], int(sys.argv[3]))
    exit(0)
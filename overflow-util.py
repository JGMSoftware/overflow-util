import sys

def printHelpInfo():
    print "\nOverflow Util Help\n==================\n"
    print "COMMANDS\n"
    print " Repeat a string n times and print it:"
    print "  overflow-util.py repeat <string to repeat> <number of times>"

def repeatString(stringToRepeat, n):
    output = stringToRepeat
    for i in range(1, n):
        output += stringToRepeat
    return output

if len(sys.argv) == 1:
    print "You need to provide some arguments. Try help"
else:
    func = sys.argv[1]
    if func == "help":
        printHelpInfo()
    if func == "repeat":
        if len(sys.argv)==4:
            repstring = sys.argv[2]
            try:
                n = int(sys.argv[3])
                print repeatString(repstring, n)
            except ValueError:
                print "You need to supply an integer for the number of repetitions."
        else:
            print "You need to supply a string to repeat and the number of times to repeat it."

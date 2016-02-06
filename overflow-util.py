import sys

def printHelpInfo():
    print "\nOverflow Util Help\n==================\n"
    print "COMMANDS\n"
    print " Repeat a string n times and print it:"
    print "  overflow-util.py repeat <string to repeat> <number of times>"
    print ""
    print " Convert an ASCII string to hexadecimal:"
    print "  overflow-util.py asciiToHex <string to convert>"
    print ""
    print " Convert a hexadecimal to ASCII:"
    print "  overflow-util.py hexToAscii <hexadecimal number (without \"0x\" prefix)>"

def repeatString(stringToRepeat, n):
    output = stringToRepeat
    for i in range(1, n):
        output += stringToRepeat
    return output

def asciiToHex(asciiString):
    hexString = "0x"
    for c in asciiString:
        hexString += str(hex(ord(c)))[2:]

    return hexString

def hexToAscii(hexString):
    return "".join(chr(int(hexString[i:i+2], 16)) for i in xrange(0, len(hexString), 2))

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
    if func == "asciiToHex":
        print asciiToHex(sys.argv[2])
    if func == "hexToAscii":
        print hexToAscii(sys.argv[2])

#!/usr/bin/python
import sys
import getopt
 
ifile=''
ofile=''
 
###############################
# o == option
# a == argument passed to the o
###############################
# Cache an error with try..except 
# Note: options is the string of option letters that the script wants to recognize, with options that require an argument followed by a colon (':') i.e. -i fileName

try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:","o=")
except getopt.GetoptError, e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)
 
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    elif o == '--o':
	print '--o'
 
# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (ifile,ofile) )

#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argPassed = "{} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argPassed += 's.'
elif argc == 1:
    argPassed += ':'
else:
    argPassed += 's:'
print(argPassed.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print("{}: {:s}".format(i, argument))
    i += 1

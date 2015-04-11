#!/usr/bin/evm python
def hex_to_per(input):
    r="{0:.2f}".format((((int (input[0:2],16))/255)*100))
    g="{0:.2f}".format((((int (input[2:4],16))/255)*100))
    b="{0:.2f}".format((((int (input[4:6],16))/255)*100))
    print(r)
    print(g)
    print(b)

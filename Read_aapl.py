'''
To read aapl.data and write the data in a new file 
Chose the format to be similar to trades.txt for consistency and readability
'''

import struct

def Read_Binary(Mkt_file):
    f = open(Mkt_file, "rb")
    g = open("aapl.txt", "w")

    list = ""
    count = 0

    while True:
        buf = f.read(4)
        if len(buf) != 4:
            break
        (pos, ) = struct.unpack("<I", buf)
        count = count + 1
        list += (str(pos) + " ")
        if (count % 5 == 0):
            g.write(list[:-1] + "\n")
            list = ""


    f.close()
    g.close()

Read_Binary('aapl.data')

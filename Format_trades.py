'''
To format the first column of trades.txt to millseconds after midnight
This can be used to compare the timestamps in both files better
'''

def Format_trades(Trd_file):
    f = open(Trd_file, 'r')
    g = open('trades_formatted.txt', 'w')

    for line in f:
        words = line[:-1].split(" ")
        # Original time - time in seconds until midnight of 2013-04-05 - 4 hours (for UTC to ET convert) * 1000 (to milliseconds)
        time_format = (int(words[0]) - 1365120000 - 14400) * 1000
        words[0] = str(time_format)
        words[3] = str(int(float(words[3]) * 100)) + "\n"
        new_line = " ".join(words)
        g.write(new_line)

    f.close()
    g.close()

Format_trades('trades.txt')

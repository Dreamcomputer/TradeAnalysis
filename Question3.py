'''
QUESTION 3:
Using the file aapl.data, compute a histogram of the spread. Ignore spreads
less than 1 cent and plot the histogram.
'''

def histogram(Mkt_file):
    spread_value = 0
    time_start = 0
    time_end = 0

    # Open file to read and the later file to write results
    f = open(Mkt_file, 'r')
    g = open('Question3_Solution.txt', 'w')
    
    for line in f:

        # Each line components into an array with omitting leading and trailing whitespace
        words = line.strip().split(" ")

        # To note the value of the spread in each line
        spread_value = int(words[2]) - int(words[4])
          
        if spread_value > 0:
            g.write(str(spread_value) + "\n")
 
    f.close()
    g.close()

    # Creating a histogram
    # Note: There are 3 outliers Outliers in the data that are not shown; 4294923195, 4294922495, 4294922495 
    # Also, interestingly these outliers occur before 9.30 am i.e., before the market is open
    import matplotlib.pyplot as plt

    Spread = []
    with open("Question3_Solution.txt") as f:
        for line in f:
            Spread.append(int(line))
    
    num_bins = 80

    n, bins, patches = plt.hist(Spread, num_bins, range=[0,80], histtype='bar',facecolor='green')

    plt.title("Spread Value Histogram")
    plt.xlabel("Spread Value")
    plt.ylabel("Frequency")
    plt.show()

histogram("aapl.txt")


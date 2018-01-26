'''
QUESTION 4:
Using the file trades.txt and aapl.data, calculate the time and price of all executions that should have taken place.
'''

def All_Trade_Executions(Mkt_file, Trd_file):

    t = open(Trd_file, 'r') 
    t_lines = t.readlines()
    t.close()

    t_list = []
    count = -1
    for t_line in t_lines:
        count += 1
        t_words = t_line.strip().split(" ")    
        t_list.append([int(t_words[0]), t_words[1], int(t_words[2]), int(t_words[3]), count])

    a = open(Mkt_file, 'r')
    a_lines = a.readlines() 
    a.close()

    a_list = []
    count = -1
    for a_line in a_lines:
        count += 1
        a_words = a_line.strip().split(" ")    
        a_list.append([int(a_words[0]), int(a_words[1]), int(a_words[2]), int(a_words[3]), int(a_words[4]), count])

    # Lines read in a_lines
    a_line_count_store = 0

    # Solution String
    solution = ""

    for t_line in t_list:
        # Current Line Data
        t_time = t_line[0]
        t_side = t_line[1]
        t_shares = t_line[2]
        t_price = t_line[3]

        for a_line in a_list[a_line_count_store:]:

            a_time = a_line[0]

            if a_time < t_time:
                a_line_count_store = a_line[5]         
            elif a_time > t_time:   

                current = a_line[5]
                a_line = a_list[current - 1]

                a_time = a_line[0]
                a_sell_shares = a_line[1]
                a_sell_price = a_line[2]
                a_buy_shares = a_line[3]
                a_buy_price = a_line[4]

                if t_side == 'S':
                    # Checking if order can be executed
                    if a_buy_shares >= t_shares and a_buy_price >= t_price:
                        #s.write("SOLD: " + str(t_time) + " At " +  str(a_time) + " for " + str(a_buy_price) + "\n")
                        solution += str(t_line) + " At " +  str(a_time) + " for " + str(a_buy_price) + "\n"
                        # Updating share count
                        a_line[3] = a_buy_shares - t_shares
                        # Executing replacement
                        a_list[current - 1][3] = a_line[3]     
                        break
                else:
                    if a_sell_shares >= t_shares and a_sell_price <= t_price:
                        #s.write("BOUGHT: " + str(t_time) + " At " +  str(a_time) + " for " + str(a_sell_price) + "\n")
                        solution += str(t_line) + " At " +  str(a_time) + " for " + str(a_sell_price) + "\n"
                        # Updating Share count
                        a_line[1] = a_sell_shares - t_shares
                        # Executing replacement
                        a_list[current - 1][1] = a_line[1]
                        break

    # Solution
    s = open('Question4_Solution.txt', 'w')
    s.write(solution)
    s.close()

All_Trade_Executions('aapl.txt', 'trades_formatted.txt')







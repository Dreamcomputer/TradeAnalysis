'''
QUESTION 5:
Suppose you are a dealer and start with 0 shares of Apple stock and must take the other side of orders in trades.txt 
that should cross in the market immediately upon order entry. Then, suppose you were given a maximum of 1 minute to 
either buy or sell those shares to get back to 0, assuming that you can trade by crossing the spread.
a) Calculate the maximum profit achievable in dollar terms.
b) Calculate the maximum gross exposure
'''

def Max_Profit_and_Exposure(Mkt_file, Trd_file):

    def Execute_trade(t_line, helper_execute_a_list):
        t_line = t_line
        helper_execute_a_list = helper_execute_a_list
        # Extracting values
        t_time = t_line[0]
        t_side = t_line[1]
        t_shares = t_line[2]
        t_price = t_line[3]

        # Value of 1 minute in millseconds (60sec * 1000)
        time_limit = 60000  

        # To keep a track of all prices that would be profitable along with the line number
        price_log = {}

        for a_line in helper_execute_a_list:
            if a_line[0] <= t_time + time_limit:
                a_buy_count = a_line[3]
                a_buy_price = a_line[4]
                a_sell_count = a_line[1]
                a_sell_price = a_line[4]
                if t_side == 'S':
                    if a_buy_count > 0:
                        price_log[a_line[5]] = a_buy_price
                else:
                    if a_buy_count > 0:
                        price_log[a_line[5]] = a_sell_price
            else:
                break

        # For profit value
        profit = 0
        # Trade Exection
        while t_shares > 0:
            if t_side == 'S':
                # Getting the line number for max price value
                max_price_a_line_number = max(price_log, key=price_log.get)
                # Getting the maximum price value in the 1 min window
                max_price = price_log.get(max_price_a_line_number)

                index = max_price_a_line_number - helper_execute_a_list[0][5]
                a_line = helper_execute_a_list[index]

                # Checking share count and deducting shares respectively
                a_buy_count = a_line[3]
                if a_buy_count >= t_shares:
                    # logging in trade executed
                    exposure_log.append([a_line[0], t_shares])
                    # Updating with remaining share count
                    helper_execute_a_list[index][3] = a_buy_count - t_shares
                    # Calculating profit
                    profit += t_shares * (max_price - t_price) 
                    t_shares = 0    
                    # RETURN values
                    return profit, helper_execute_a_list
                else:
                    # logging in trade executed
                    exposure_log.append([a_line[0], a_buy_count])
                    # Updating with remaining shares
                    helper_execute_a_list[index][3] = 0
                    # Calculating profit
                    profit += a_buy_count * (max_price - t_price)
                    t_shares += -a_buy_count
                    # Remove item in dictionary upon exhaustion of shares
                    del price_log[max_price_a_line_number]
            else:
                # Getting the line number for min price value
                min_price_a_line_number = min(price_log, key=price_log.get)
                # Getting the maximum price value in the 1 min window
                min_price = price_log.get(min_price_a_line_number)

                index = min_price_a_line_number - helper_execute_a_list[0][5]
                a_line = helper_execute_a_list[index]

                # Checking share count and deducting shares respectively
                a_sell_count = a_line[1]
                if a_sell_count >= t_shares:
                    # logging in trade executed
                    exposure_log.append([a_line[0], t_shares])
                    # Updating with remaining share count
                    helper_execute_a_list[index][1] = a_sell_count - t_shares
                    # Calculating profit
                    profit += t_shares * (t_price - min_price) 
                    t_shares = 0    
                    # RETURN values
                    return profit, helper_execute_a_list
                else:
                    # logging in trade executed
                    exposure_log.append([a_line[0], a_sell_count])
                    # Updating with remaining shares
                    helper_execute_a_list[index][1] = 0
                    # Calculating profit
                    profit += a_sell_count * (t_price - min_price)
                    t_shares += -a_sell_count
                    # Remove item in dictionary upon exhaustion of shares
                    del price_log[min_price_a_line_number]



    ##########################
    ######## MAIN FUNCTION
    ##########################

    Instant_profit = 0  
    # Denotes the total shares accepted without the executed trade shares being deducted
    total_shares = 0
    # Initializing a dictionary for storing [timestamp, shares] in helper function 
    exposure_log = [] 
    # To keep track of gross exposure values at each execution
    gross_exposure = []
    # Store total profit
    total_profit = 0

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

    # To keep track of available shares in the market while accepting/rejecting an order
    a_list = []
    # To keep track of available shares in execution of accepted trades
    execute_a_list = []
    count = -1
    for a_line in a_lines:
        count += 1
        a_words = a_line.strip().split(" ")    
        a_list.append([int(a_words[0]), int(a_words[1]), int(a_words[2]), int(a_words[3]), int(a_words[4]), count])
        execute_a_list.append([int(a_words[0]), int(a_words[1]), int(a_words[2]), int(a_words[3]), int(a_words[4]), count])

    # Lines read in a_lines
    a_line_count_store = 0

    for t_line in t_list:
        # Current Line Data
        t_time = t_line[0]
        t_side = t_line[1]
        t_shares = t_line[2]
        t_price = t_line[3]

        for a_line in a_list[a_line_count_store:]:

            a_time = a_line[0]

            #if a_time < t_time:
              #  a_line_count_store = a_line[5]         
            #elif a_time > t_time:       
            if a_time > t_time:  
                current = a_line[5]
                a_line = a_list[current - 1]
                a_line_count_store = current - 1

                a_time = a_line[0]
                a_sell_shares = a_line[1]
                a_sell_price = a_line[2]
                a_buy_shares = a_line[3]
                a_buy_price = a_line[4]

                if t_side == 'S':
                    # Checking if order can be executed
                    if a_buy_shares >= t_shares and a_buy_price >= t_price:
                        # Updating share count
                        a_line[3] = a_buy_shares - t_shares
                        a_list[current - 1][3] = a_line[3] 

                        ######## TOTALPROFIT, Instant profit and GROSS EXPOSURE
                        Instant_profit += t_shares * (a_buy_price - t_price) 
                        # Total shares until this point not deducting the executed orders 
                        total_shares += t_shares 
                        executed_shares = 0 # for using below to count executed shares until this point
                        # Storing the gross exposure value at this point
                        if exposure_log: #If list is not empty
                            for execution in exposure_log:
                                if execution[0] <= t_time:
                                    executed_shares += execution[1]

                        # Storing current gross exposure value
                        gross_exposure.append([str(t_time), (total_shares - executed_shares) * a_buy_price])
                            
                        # Executing order under 1 min, getting profit from order execution and updated a_execute_lines with shares
                        helper_execute_a_list = execute_a_list[a_line_count_store:]
                        sell_profit, new_a_execute_list = Execute_trade(t_line, helper_execute_a_list)

                        # Calculating Total profit
                        total_profit += sell_profit

                        # Modying all lines in a_lines with updated shares
                        execute_a_list[a_line_count_store:] = new_a_execute_list
                        break                            
                else:
                    if a_sell_shares >= t_shares and a_sell_price <= t_price:
                        # Updating Share count
                        a_line[1] = a_sell_shares - t_shares
                        a_list[current - 1][1] = a_line[1]

                        ######## TOTALPROFIT, Instant profit and GROSS EXPOSURE
                        Instant_profit += t_shares * (t_price - a_sell_price) 
                        # Total shares until this point not deducting the executed orders 
                        total_shares += t_shares 
                        executed_shares = 0 # for using below to count executed shares until this point
                        # Storing the gross exposure value at this point
                        if exposure_log: #If list is not empty
                            for execution in exposure_log:
                                if execution[0] <= t_time:
                                    executed_shares += execution[1]

                        # Storing current gross exposure value
                        gross_exposure.append([str(t_time), (total_shares - executed_shares) * a_sell_price])
                            
                        # Executing order under 1 min, getting profit from order execution and updated a_execute_lines with shares
                        helper_execute_a_list = execute_a_list[a_line_count_store:]
                        buy_profit, new_a_execute_list = Execute_trade(t_line, helper_execute_a_list)

                        # Calculating Total profit
                        total_profit += buy_profit

                        # Modying all lines in a_lines with updated shares
                        execute_a_list[a_line_count_store:] = new_a_execute_list  
                        break
                break

    print ("TOTAL PROFIT IN DOLLARS: " + str(total_profit/100))
    print ("INSTANT Profit IN DOLLARS: " + str(Instant_profit/100))

    max_exposure = max(gross_exposure, key=lambda x: x[1])
    # Getting the time at which there was maximum exposure
    max_exposure_time = max_exposure[0]
    # Getting the maximum exposure
    max_exposure_value = max_exposure[1]

    print ("Max gross exposure IN DOLLARS: " + str(max_exposure_value/100) + " at time: " + str(max_exposure_time)) 

Max_Profit_and_Exposure('aapl.txt', 'trades_formatted.txt')









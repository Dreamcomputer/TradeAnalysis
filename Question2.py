'''
QUESTION 2:
Using the file aapl.data, compute the percentage of time the market was crossed or 
locked for AAPL on this trading day.
'''

def Pc_Mkt_Locked_Crossed_Time(Mkt_file):
    
    # Global Variables to keep track of time and duration of Mkt Locked/Crossed events
    global_first_time = 0
    global_second_time = 0
    log_time = 0

    # List to keep track of events of the same timestamp, for a more accurate calculation of time duration
    same_time_list = []
    # To remember the time of Mkt Locked/Crossed event
    remember_time = 0

    f = open(Mkt_file, 'r')
    for line in f:            
        # Getting Values from each line
        words = line.strip().split(" ")
             
        id = int(words[0])
        ask_price = int(words[2])
        bid_price = int(words[4])
        global_second_time = id

        # Adding time to time track list
        same_time_list.append(id)

        # Calculating fraction of log_time if any
        l = len(same_time_list)
        if l > 1:
            if (same_time_list[l - 1] != same_time_list[l - 2]):
                if same_time_list[l - 2] == remember_time and (l - 2) > 0:
                    extra_log_time = 1 / (l - 1) 
                    log_time += extra_log_time
                
                same_time_list = [same_time_list.pop()]
        if global_first_time != 0:
            log_time += global_second_time - global_first_time 
        if ask_price <= bid_price:
            global_first_time = id
            remember_time = id
        else:
            global_first_time = 0
            global_second_time = 0

    # Closing file
    f.close()

    # Total Market time = 9.30am to 4pm in millseconds (6.5hrs * 60 * 60 * 1000)
    total_mkt_time = 23400000
         
    # Percentage of market time locked/crossed = log_time/total_mkt_time * 100 
    percentage_Mkt_Crossed_Locked_Time = log_time/total_mkt_time * 100

    return percentage_Mkt_Crossed_Locked_Time

# Call function
Answer = Pc_Mkt_Locked_Crossed_Time("aapl.txt")
# Print answer
print ("Percentage of time the market was Crossed or Locked for AAPL on this trading day: " + str(Answer))
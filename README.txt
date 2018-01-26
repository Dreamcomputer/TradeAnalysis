-------------------------------------------------------------------------------
-- ORDER OF EXECUTION
-------------------------------------------------------------------------------
Note: From Question 2 to 5, “aapl.txt” and “trades_formatted.txt” are used to run.
 
1. Run Read_aapl.py, which will output the file aapl.txt (formatted version similar to the given trades.txt)

2. Run Format_trades.py, which will output the file trades_formatted.txt. This is so that the timestamp in give trades.txt is now displayed as milliseconds after midnight of 2013-04-05. It makes it easier for comparison with apple.data

3. Question2.py will print out in the terminal, the percentage of time that the market was crossed or locked for AAPL on the given trading day.

4. Question3.py will give out Question3_Solution.txt, which displays the spread value for every tick of apple.data, along with a histogram.
There is another folder Question3_Extra that contains Question3_With_Timespan.py that gives out a solution file with spread for every tick in apple.data along with the time_duration. Doesn’t give out a histogram yet, need to discuss for producing one.
NOTE: Might have to install python’s matplotlib to be able to see the histogram. Try the following command in terminal if you don’t already have it: 
pip install matplotlib

5. Question4.py will give out Question4_Solution.txt which contains trade information and the time and price the trade was executed at.

6. Question5.py will print out in the terminal, the (i) Maximum Profit achievable (ii) Instant Profit i.e., when executed instantly (iii) Maximum Gross Exposure

-------------------------------------------------------------------------------
-- Solution Comments
-------------------------------------------------------------------------------

1. The condition of locked or crossed markets is closely related to a
classic problem in distributed systems. Explain why it is impossible
to completely avoid markets crossing.
SOLUTION: This is commonly known as the consistency problem in distributed systems. All the various stock exchanges(such as NQ, NYSE, BATS, CHX, NSX etc) act as components of the distributed system and when two or more almost simultaneous changes occur in the same data (for instance, stocks being bought from the same lot at the same time at both NQ and NYSE), the updates would reach the server at slightly different times and before the second component is notified of the first component’s update message, it would have already processed an order which would otherwise not be executed. In the market, these updates occur in microseconds/milliseconds which means extremely rapid exchange of messages across different components making it hard for synchronization at times. Also, the CAP theorem states that it is impossible for a distributes system to guarantee consistency, availability and partition tolerance at the same time. Usually two of the three are guaranteed. 

5. Suppose you are a dealer and start with 0 shares of Apple stock and must
take the other side of orders in trades.txt that should cross in the market
immediately upon order entry. Then, suppose you were given a maximum of 1
minute to either buy or sell those shares to get back to 0, assuming that you
can trade by crossing the spread.
a) Calculate the maximum profit achievable in dollar terms.
b) Calculate the maximum gross exposure.
COMMENTS:

A. There are 2 cases:
Note: Took shares into account as well in addition to price, to avoid situations where client asked for a million shares and the market is dealing with only 500 shares for the price. If we didn’t execute the share condition, in real life, we might be at a risk of huge loss trying to sell/buy a million shares while market’s range is 500 - 1000.
CASE 1: (What I followed in the solution): When we accept orders from client based purely on market price and available shares.
CASE 2: When we accept orders from client based on market price and available shares based on our previous trade executions, then we accept a few lesser shares. (Approx 5)
 
What happens for the above trades in Case 2 is that at the corresponding “aapl.data time” and “Mkt price at that time” the shares were used up by the orders that we accepted prior (because the price at which those shares were offered make the best profit for those) to the mentioned above orders.

However, in the given data, CASE 1 Total profit* = $119,477.89 is slightly higher than CASE 2 Total profit. Would be interesting to see for different data sets.

Note: 
1*. Calculated profit based on executed price - client price
Another way to calculate if the client sent us the orders expecting us to execute with the current market rate, then we would follow CASE 2 approach (it ensures that we are surely not at loss in this situation) and our profit would be calculated based on executed price  - then current market price and client’s profit would be then current market price - client’s given price
2.Conditions mentioned above can be modified in a split of a second based on the structure of the code, please let me know if you’d like to see any alternates (such as below)

B. 
Quick sanity check to check the gross exposure correctness:
At 53509000 to 1 minute before that, there are huge number of shares in the trade orders, combined, unlike any other chunk in the trades.txt file

C.
For the case when we have MULTIPLE market data tick timestamp = trade order timestamp,
I conservatively used the last tick in the market data for a given time stamp to check if we accept the order or not.
I can use any other logic such as the below (Let me know if you'd like to see):
a. Check if the trade order can be executed for any of all the market data ticks at that time.
b. If we have 2 orders at the same millisecond, and 10 market data ticks in for the same millisecond,
we can check the 1st order against the first 5 market data ticks and the 2nd order against the later 5
market data ticks. (This is an example of how data in microsecond level can be helpful, or at least 
Trade order data in millisecond level).

D. The comparison approach
Consider the following scenario:
 Trade 1 =  100 shares at $1 each
 Trade 2 = 200 shares at $2 each

Now, according to the market data the best price for the above trade orders are:
Ticker 1 = 200 shares at $3 each [BEST PRICE for BOTH trades]
Ticker 2 = 250 shares at $2 each [Second best for Trade 1]
Ticker 3 = 200 shares at $1 [Second best for Trade 2]

(Partial orders enabled in both approaches:
Regular approach: 
When we execute these trades in our regular approach of executing Trade 1 first, then profit is the below:
100 shares * ($3 - $1) + 100 shares * ($3 - $2) + 100 shares * ($1 - $2) = $200
Comparison approach:
In this approach we check, on executing which order first will be make the most profit. I’ve written down an algorithm for this if you want to discuss. the result of the comparison approach in the above case with be:
200 shares * ($3 - $2) + 100 shares * ($2 - $1) = $300 

Some questions regarding question 5: (Write questions mentioned in Question paper)
a. Gross Exposure in shares or price value: Not sure if you wanted to see exposure in terms of Number of Shares or Price value, used current price value in my approach
b. Matching the orders: If the client wants to see and buy shares within the same minute, then can we not go to the market and just match their orders instead (Incase that is the best profit case)


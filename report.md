Max Profit Finder 

Course: CS314 — Analysis of Algorithms
Topic: Divide and Conquer
Project level: Beginner

1. Problem Description

The goal of this project is to find the maximum profit that can be achieved from one transaction: buy on one day and sell on a later day. The program receives a sequence of daily prices from a CSV file and reports the buying day, selling day, and maximum profit.

The project compares two approaches to the same problem:

A Divide and Conquer solution based on the maximum-subarray problem.

A Linear Scan solution that checks the prices in one pass.

The included prices.csv contains sample educational data only. It is not real stock-market data and should not be used for financial decisions.

2. Method

2.1 Convert prices into daily changes

Instead of searching directly for two prices, the program calculates the change between each pair of consecutive days:

change[i] = price[i + 1] - price[i]

A consecutive group of positive and negative changes represents the profit or loss over a buy/sell period. Therefore, the best transaction corresponds to the maximum-sum contiguous subarray of the changes.

2.2 Divide and Conquer

The Divide and Conquer method splits the changes array into two halves. It recursively finds three possible answers:

The maximum subarray completely inside the left half.

The maximum subarray completely inside the right half.

The maximum subarray that crosses the midpoint.

For the crossing case, the program finds the best suffix of the left half and the best prefix of the right half, then adds them. The algorithm returns the largest of the three results. When the range contains one element, that element is the base case.

The recurrence is:

T(n) = 2T(n/2) + Θ(n)

There are two recursive calls on half-size inputs, and the crossing calculation takes linear time. By the Master Theorem, the running time is:

T(n) = Θ(n log n)

2.3 Linear Scan

The Linear Scan method keeps the lowest price seen so far. For every later day, it calculates the profit that would result from selling on that day. It updates the best transaction whenever a larger profit is found.

Each price is visited once, so its time complexity is:

T(n) = Θ(n)

If every later price is equal to or lower than the buying price, both methods report that no profitable transaction exists.

3. Experiments

The program measures both algorithms with time.perf_counter. For each input size, both algorithms receive the same generated sequence of prices. The tested sizes are 100, 500, 1,000, 2,000, 4,000 and 8,000 prices.

The generated measurements are saved in benchmark_results.csv, and the comparison is plotted in benchmark_chart.png. One sample run produced the following approximate results; exact times may differ between computers:

Input size

Divide and Conquer (s)

Linear Scan (s)

100

0.000391

0.000009

500

0.001062

0.000034

1,000

0.001985

0.000066

2,000

0.004068

0.000126

4,000

0.008451

0.000276

8,000

0.019795

0.000907

The results show that Linear Scan is faster for these tests. This agrees with the theoretical analysis: linear growth is lower than n log n growth. The experiment is illustrative; execution times depend on hardware, background processes and the Python environment.

4. Correctness and Testing

The program checks that both approaches return the same maximum profit for the CSV input. The unit tests cover:

A sequence with a profitable transaction.

A decreasing sequence with no profitable transaction.

An input containing only one price.

A case where the best selling day is the final day.

All four unit tests passed in the validation run.

5. Conclusion

The project demonstrates how the maximum-subarray problem can be used to solve the best buy-and-sell problem with Divide and Conquer. This approach has Θ(n log n) running time. The Linear Scan method solves the same task in Θ(n) time and performs better in the measured experiments.

The main lesson is that Divide and Conquer is an important general design technique, but a simpler linear solution can be more efficient when the problem structure allows it.

6. Reflection

The most useful observation was that both algorithms produce the same answer even though their strategies and running times differ. If the project were extended, it could accept a larger real historical-price CSV and compare the algorithms on more datasets.
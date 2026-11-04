import time
import random
import pandas as pd
import matplotlib.pyplot as plt


def max_crossing_sum(changes, low, mid, high):
    left_sum = float("-inf")
    total = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        total += changes[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float("-inf")
    total = 0
    max_right = mid + 1

    for i in range(mid + 1, high + 1):
        total += changes[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return left_sum + right_sum, max_left, max_right


def max_subarray(changes, low, high):
    if low == high:
        return changes[low], low, high

    mid = (low + high) // 2

    left_result = max_subarray(changes, low, mid)
    right_result = max_subarray(changes, mid + 1, high)
    cross_result = max_crossing_sum(changes, low, mid, high)

    return max(left_result, right_result, cross_result, key=lambda result: result[0])


def divide_and_conquer_profit(prices):
    if len(prices) < 2:
        return 0, None, None

    changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    profit, buy_index, sell_index = max_subarray(changes, 0, len(changes) - 1)

    if profit <= 0:
        return 0, None, None

    return profit, buy_index, sell_index + 1


def linear_scan_profit(prices):
    if len(prices) < 2:
        return 0, None, None

    min_price = prices[0]
    min_index = 0
    best_profit = 0
    buy_index = None
    sell_index = None

    for i in range(1, len(prices)):
        current_profit = prices[i] - min_price

        if current_profit > best_profit:
            best_profit = current_profit
            buy_index = min_index
            sell_index = i

        if prices[i] < min_price:
            min_price = prices[i]
            min_index = i

    return best_profit, buy_index, sell_index


def run_benchmark():
    sizes = [100, 500, 1000, 2000, 4000, 8000]
    divide_times = []
    linear_times = []

    random.seed(42)

    for size in sizes:
        prices = [100.0]
        for _ in range(size - 1):
            prices.append(max(1.0, prices[-1] + random.uniform(-2, 2)))

        start = time.perf_counter()
        divide_and_conquer_profit(prices)
        divide_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        linear_scan_profit(prices)
        linear_times.append(time.perf_counter() - start)

    results = pd.DataFrame({
        "Input Size": sizes,
        "Divide and Conquer (seconds)": divide_times,
        "Linear Scan (seconds)": linear_times
    })
    results.to_csv("benchmark_results.csv", index=False)

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, divide_times, marker="o", label="Divide and Conquer")
    plt.plot(sizes, linear_times, marker="o", label="Linear Scan")
    plt.xlabel("Number of Daily Prices")
    plt.ylabel("Running Time (seconds)")
    plt.title("Max Profit Finder: Running Time Comparison")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("benchmark_chart.png", dpi=200)
    plt.close()


def main():
    data = pd.read_csv("prices.csv")

    if "Day" not in data.columns or "Price" not in data.columns:
        raise ValueError("prices.csv must contain Day and Price columns.")

    days = data["Day"].tolist()
    prices = data["Price"].astype(float).tolist()

    if len(prices) < 2:
        raise ValueError("The CSV file must contain at least two prices.")

    divide_result = divide_and_conquer_profit(prices)
    linear_result = linear_scan_profit(prices)

    print("MAX PROFIT FINDER")
    print("-----------------")
    print("Divide and Conquer:")
    print_result(divide_result, days, prices)

    print("\nLinear Scan:")
    print_result(linear_result, days, prices)

    if divide_result[0] != linear_result[0]:
        raise RuntimeError("The two algorithms returned different profits.")

    run_benchmark()
    print("\nBenchmark files created: benchmark_results.csv and benchmark_chart.png")


def print_result(result, days, prices):
    profit, buy_index, sell_index = result

    if buy_index is None:
        print("No profitable transaction.")
        print("Maximum Profit: 0")
        return

    print(f"Buy Day: {days[buy_index]} at {prices[buy_index]:.2f}")
    print(f"Sell Day: {days[sell_index]} at {prices[sell_index]:.2f}")
    print(f"Maximum Profit: {profit:.2f}")


if __name__ == "__main__":
    main()

import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    max_val = float('inf')
    dp = [0] + [max_val] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i] == dp[i - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                i -= coin
                break

    return result

def compare_algorithms(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Greedy Algorithm: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming: {dp_result}, Time: {dp_time:.6f} seconds")

# Приклад використання
compare_algorithms(10143)

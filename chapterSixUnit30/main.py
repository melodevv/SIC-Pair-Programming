# =========================================
#              QUESTION ONE
# =========================================
def coin_change(coins, wallet, amount):
    changes = []
    largest = 0
    while amount > 0:
        if amount < coins[largest] or wallet[largest] == 0:
            largest += 1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]
            wallet[largest] -= 1
    return changes


coins = [500, 100, 50, 10]
wallet = [1, 1, 3, 2]          # list for number of available coins in the wallet
amount = int(input('Input the amount: '))
changes = coin_change(coins, wallet, amount)
print(changes, len(changes))


# =========================================
#              QUESTION TWO
# =========================================
def coins_change2(coins, amount):
    changes = []
    largest = 0

    while amount > 0:
        if amount < coins[largest]:
            largest += 1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]
            largest += 1
    return changes


coins2 = list(map(int, input("Input the coins: ").split()))
coins2.sort(reverse=True)
print(coins2)
amount2 = int(input("Input the amount: "))
changes2 = coins_change2(coins2, amount2)
print(changes2, len(changes2))

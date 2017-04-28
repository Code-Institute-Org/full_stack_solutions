from decimal import *

coins = [1, .50, .20, .10, .05, .02, .01]


def give_change(amount):
    change = []
    # The amount is converted to a string then a decimal
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            # No floating point errors as we are using only decimals
            amount -= coin
            change.append(float(coin))
    return change

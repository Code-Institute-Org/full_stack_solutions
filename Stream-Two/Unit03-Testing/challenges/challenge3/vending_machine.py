from decimal import Decimal

coins = [1, .50, .20, .10, .05, .02, .01]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}


def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change


def give_item_and_change(item, amount):
    if item not in available_items:
        return None, amount, "that item isn't available"

    cost = available_items[item]

    if amount < cost:
        return None, amount, 'not enough money'

    change_to_return = amount - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change"


if __name__ == '__main__':
    while True:
        item = raw_input('choose item: %s' % available_items)
        amount = input('enter amount in pounds:')
        print give_item_and_change(item, amount)

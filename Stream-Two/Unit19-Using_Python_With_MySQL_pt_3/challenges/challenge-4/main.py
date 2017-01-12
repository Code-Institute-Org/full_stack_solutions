import random
from database.mysql import MySQLDatabase
from settings import db_config


"""
Retrieve the settings from the
`db_config` dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""
db = MySQLDatabase(db_config.get('db_name'),
                   db_config.get('user'),
                   db_config.get('pass'),
                   db_config.get('host'))

# Select a person from the people table
person = db.select('people', named_tuples=True, where="id=2")[0]
print person

# Select all orders for that person
orders = db.select('orders', named_tuples=True,
                   where="person_id=%s" % person.id)
print orders

# Iterate over each order
for order in orders:
    print order
    # Update the amount of each order
    db.update('orders', where="id=%s" % order.id, amount="20.02")

# Select all the orders for that person again
new_orders = db.select('orders', named_tuples=True,
                       where="person_id=%s" % person.id)

# Iterate over the orders and print
# out each one to ensure that the
# amount column has been updated.
for order in new_orders:
    print order

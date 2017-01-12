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

# Insert a new person into the people table
db.insert('people', first_name="April", second_name="ONeil",
          DOB='STR_TO_DATE("02-10-1984", "%d-%m-%Y")')

# Retrieve the new person from the people table
april = db.select('people', ["id", "first_name"], where='first_name="April"',
                  named_tuples=True)
# We only need the first entry in the list
april = april[0]

# Insert into the profiles table using the
# id of the 'april' person
db.insert('profiles', person_id="%s" % april.id,
          address="New York City")

# Insert into the orders table using the
# id of the person and generate a random
# integer for the amount column
db.insert('orders', person_id="%s" % april.id,
          amount="%s" % random.randint(2, 18))

db.insert('orders', person_id="%s" % april.id,
          amount="%s" % random.randint(2, 18))

# Retrieve all the orders for the the 'april' person
# using the id
orders = db.select('orders', where='person_id=%s' % april.id)

# Iterate over the list of results and
# print each one out to the console
for order in orders:
    print order

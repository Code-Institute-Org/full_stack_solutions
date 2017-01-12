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

# Get all the available tables for
# our database annd print them out.
tables = db.get_available_tables()
print tables

# Get all the available columns for our
# articles table and print them out
columns = db.get_columns_for_table('people')
print columns

# Get all the records from
# the people table
results = db.select('people')

for row in results:
    print row


# Selecting columns with named tuples
results = db.select('people',
                    columns=['id', 'first_name'], named_tuples=True)

for row in results:
    print row.id, row.first_name

# We can also do more complex queries using `CONCAT`
# and `SUM`
people = db.select('people', columns=["CONCAT(first_name, ' ', second_name)"
                                      " AS full_name", "SUM(amount)"
                                      " AS total_spend"],
                   named_tuples=True, where="people.id=1",
                   join="orders ON people.id=orders.person_id")

for person in people:
    print person.full_name, "spent ", person.total_spend

# Inserting an order
db.insert('orders', person_id="2", amount="120.00")

# Updating a person
person = db.select('people', named_tuples=True)[0]

db.update('profiles', where="person_id=%s" % person.id,
          address="1a another street")

# Deleting a record
person = db.select('people', named_tuples=True)[0]
db.delete('orders', person_id="=%s" % person.id, id="=1")

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

# Get all the available columns for our 
# orders table and print them out
columns = db.get_columns_for_table('orders')
print columns
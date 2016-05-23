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

# Select using the limit clause
limited_results = db.select('orders', limit='5')
print "--------------------------------------"
print "First 5 Results"
print "--------------------------------------"
# iterate over the list of results
for result in limited_results:
	print result
print "--------------------------------------"

# Limit the results to 10
limited_results = db.select('orders', limit='10')
print "First 10 results"
print "--------------------------------------"
for result in limited_results:
	print result
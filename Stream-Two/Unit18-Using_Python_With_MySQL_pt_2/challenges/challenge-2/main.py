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

descending_results = db.select('orders', order_desc='amount')
print "--------------------------------------"
print "Descending Results -"
print "--------------------------------------"
for result in descending_results:
	print result

ascending_results = db.select('orders', order_asc='amount')
print "--------------------------------------"
print "Ascending Results -"
print "--------------------------------------"
for result in ascending_results:
	print result
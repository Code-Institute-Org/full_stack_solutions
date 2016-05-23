import random
from database.mysql import MySQLDatabase
from settings import db_config


if __name__ == "__main__":
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
	
	# Select all orders for that person
	orders = db.select('orders', named_tuples=True, 
						where="person_id=%s" % person.id)

	# Print out each of the records
	for order in orders:
		print order

	# Execute the delete function without
	# `id='=1'` argument to see what happens
	db.delete('orders', person_id="=%s" % person.id)

	# Select all the order records for that
	# person again, so we can the effect it will
	# have
	orders = db.select('orders', where="person_id=%s" % person.id)

	# This won't actually print out
	# anything because all the records
	# have been deleted causing
	# the select to return an empty list
	for order in orders:
		print order
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

	# Retrieve the first_name column and get the average
	# amount spent where the person.id = 1
	people = db.select('people', columns=["first_name", "AVG(amount)" \
										  " AS average_spent"],
					   named_tuples=True, where="people.id=1",
					   join="orders ON people.id=orders.person_id")

	# Print the results in a format that
	# looks like - "<first_name> spends <average_amount>"
	for person in people:
		print person.first_name, "spends", person.average_spent

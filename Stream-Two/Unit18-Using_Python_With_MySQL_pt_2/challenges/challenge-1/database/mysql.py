import MySQLdb as _mysql
from collections import namedtuple


class MySQLDatabase(object):
	"""
	This is the driver class that we will use
	for connecting to our database. In here we'll
	create a constructor (__init__) that will connect
	to the database once the driver class is instantiated
	and a destructor method that will close the database
	connection once the driver object is destroyed.
	"""

	def __init__(self, database_name, username,
				 password, host='localhost'):
		"""
		Here we'll try to connect to the database
		using the variables that we passed through
		and if the connection fails we'll print out the error
		"""
		try:
			self.db = _mysql.connect(db=database_name, host=host,
									 user=username, passwd=password)
			self.database_name = database_name
			print "Connected to MySQL!"
		except _mysql.Error, e:
			print e

	def __del__(self):
		"""
		Here we'll do a check to see if `self.db` is present.
		This will only be the case if the connection was 
		successfully made in the initialiser.
		Inside that condition we'll close the connection
		"""
		if hasattr(self, 'db'):
			self.db.close()
			print "MySQL Connection Closed"

	def get_available_tables(self):
		"""
		This method will allow us to what
		tables are available to us when we're 
		running our queries
		"""
		cursor = self.db.cursor()
		cursor.execute("SHOW TABLES;")
		self.tables = cursor.fetchall()

		cursor.close()

		return self.tables

	def convert_to_named_tuples(self, cursor):
		results = None
		names = " ".join(d[0] for d in cursor.description)
		klass = namedtuple('Results', names)

		try:
			results = map(klass._make, cursor.fetchall())
		except _mysql.ProgrammingError, e:
			print e

		return results

	def get_columns_for_table(self, table_name):
		"""
		This method will enable to interact
		with our database to find what columns
		are currently in a specific table
		"""
		cursor = self.db.cursor()
		cursor.execute("SHOW COLUMNS FROM `%s`" % table_name)
		self.columns = cursor.fetchall()

		cursor.close()

		return self.columns

	def select(self, table, columns=None, named_tuples=False, **kwargs):
		"""
		We'll create our `select` method in order
		to make it simpler for extracting data from
		the database.
		select(table_name, [list_of_column_names])
		"""
		sql_str = "SELECT "

		# add columns or just use the wilcard
		if not columns:
			sql_str += " * "
		else:
			for column in columns:
				sql_str += "%s, " % column

			sql_str = sql_str[:-2] # remove the last comma!

		# add the to the SELECT query
		sql_str += " FROM `%s`.`%s`" % (self.database_name, table)

		# if there's a JOIN clause attached
		if kwargs.has_key('join'):
			sql_str += " JOIN %s" % kwargs.get('join')

		# if there's a WHERE clause attached
		if kwargs.has_key('where'):
			sql_str += " WHERE %s " % kwargs.get('where')

		# if there's a LIMIT clause attached
		if kwargs.has_key('limit'):
			sql_str +=" LIMIT %s" % kwargs.get('limit')

		sql_str += ";" # Finalise out SQL string

		cursor = self.db.cursor()
		cursor.execute(sql_str)

		if named_tuples:
			results = self.convert_to_named_tuples(cursor)
		else:
			results = cursor.fetchall()

		cursor.close()

		return results

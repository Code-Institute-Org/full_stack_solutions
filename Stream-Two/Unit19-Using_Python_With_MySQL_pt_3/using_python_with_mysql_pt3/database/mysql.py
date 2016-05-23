import MySQLdb as _mysql
from collections import namedtuple
import re

# Only needs to compile one time so we put it here
float_match = re.compile(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$').match


def is_number(string):
	return bool(float_match(string))


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

		sql_str += ";" # Finalise out SQL string

		cursor = self.db.cursor()
		cursor.execute(sql_str)

		if named_tuples:
			results = self.convert_to_named_tuples(cursor)
		else:
			results = cursor.fetchall()

		cursor.close()

		return results

	def insert(self, table, **column_names):
		"""
		Insert function.

		Example Usage:-
		db.insert('people', first_name='Ringo', 
				  second_name='Starr', DOB=STR_TO_DATE(
				  						   '01-01-1999', '%d-%m-%Y'))
		"""
		sql_str = "INSERT INTO `%s`.`%s` " % (self.database_name, table)

		if column_names is not None:
			columns = "("
			values = "("
			for arg, value in column_names.iteritems():
				columns += "`%s`, " % arg

				# Check how we should add this to the columns string
				if is_number(value):
					# It's a number so we don't add the ''
					values += "%s, " % value
				else:
					# It's a date or a string so we add the ''
					values += "'%s', " % value

			columns = columns[:-2] # Strip off the spare',' from the end
			values = values[:-2] # Same here too

			columns += ") VALUES" # Add the connecting keyword and brace
			values += ");" # Add the brace and like terminator

			sql_str += "%s %s" % (columns, values)

		cursor = self.db.cursor()
		cursor.execute(sql_str)
		self.db.commit()
		cursor.close()

	def delete(self, table, **wheres):
		"""
		This function will allow us
		to delete data from a given table
		based on whether or not a WHERE
		clause is present or not
		"""
		sql_str = "DELETE FROM `%s`.`%s` " % (self.database_name, table)

		if wheres is not None:
			first_where_clause = True
			for where, term in wheres.iteritems():
				if first_where_clause:
					# This is the first WHERE clause
					sql_str += " WHERE `%s`.`%s`%s" % (table, where, term)
					first_where_clause = False
				else:
					# this is an additional clause so use AND
					sql_str += " AND `%s`.`%s`%s" % (table, where, term)
		sql_str += ";"

		cursor = self.db.cursor()
		cursor.execute(sql_str)
		self.db.commit()
		cursor.close()

	def update(self, table, where=None, **column_names):
		"""
		Update Function.

		This function will allows to 
		update any records in our database.

		Example Usage:-
		db.update('people', where="id=1")
		"""
		sql_str = "UPDATE `%s`.`%s` SET " % (self.database_name, table)

		if column_names is not None:
			for column_name, value in column_names.iteritems():
				sql_str += "`%s`=" % column_name

				# Check how we should add this to the columns string
				if is_number(value):
					# It's a number so we don't add ''
					sql_str +="%s, " % value
				else:
					# It's a date or a string so add the ''
					sql_str += "'%s', " % value
			sql_str = sql_str[:-2] # Strip off the last , and space character

			if where:
				sql_str += " WHERE %s" % where

			cursor = self.db.cursor()
			cursor.execute(sql_str)
			self.db.commit()
			cursor.close()

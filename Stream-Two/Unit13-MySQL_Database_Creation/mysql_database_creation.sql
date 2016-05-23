/**
 * Create a MySQL Database
 */
CREATE DATABASE my_db;


/**
 * Tell MySQL which Database we wish to use
 */
USE my_db;


/**
 * Create a table called people that will
 * have the following rows - 
 * id, first_name, second_name, DOB
 */
CREATE TABLE people (
	id INTEGER AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
	second_name VARCHAR(50) NOT NULL,
	DOB DATE NOT NULL,
	PRIMARY KEY (id)
);


/**
 * Create another table that references the `people` table
 * using a foreign key relationship.
 */
CREATE TABLE orders(
	id INTEGER AUTO_INCREMENT,
	amount DECIMAL(18,2) NOT NULL,
	person_id INT,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (person_id) REFERENCES people(id),
	CHECK(amount>0)
);


/**
 * Create an index for the `people` table 
 * using the first_name field
 */
CREATE INDEX first_name_index ON people (first_name);
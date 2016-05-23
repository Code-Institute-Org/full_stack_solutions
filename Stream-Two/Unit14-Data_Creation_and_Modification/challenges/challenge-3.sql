USE my_db;

/**
 * Drop all our tables by using the `DROP TABLE` query
 */
DROP TABLE profiles;
DROP TABLE orders;
DROP TABLE people;

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
 * Create a new table called `profiles`
 */
CREATE TABLE profiles (
	id INTEGER AUTO_INCREMENT,
	person_id INT,
	address text,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (person_id) REFERENCES people(id)
);

/**
 * Add a new row into our `people` table
 */
INSERT INTO `my_db`.`people` (
	`first_name`,
	`second_name`,
	`DOB`
) VALUES (
	"Wally",
	"West",
	STR_TO_DATE("05-02-1991", "%d-%m-%Y")
);

/**
 * Add our person to the `profile` table
 */
INSERT INTO `my_db`.`profiles` (
	`person_id`,
	`address`
) VALUES (
	1,
	"Central City"
);

/**
 * Create five orders using a single INSERT command
 */
INSERT INTO `my_db`.`orders` (
	`amount`,
	`person_id`
) VALUES 
	(17.05, 1),
	(2.99, 1),
	(8.00, 1),
	(7.75, 1),
	(13.14, 1);
USE my_db;


/**
 * Create a new table called `articles`
 */
CREATE TABLE articles (
	id INTEGER AUTO_INCREMENT,
	title VARCHAR(200),
	content TEXT,
	person_id INT NOT NULL,
	PRIMARY KEY(id)
);


/**
 * Insert some data into our newly created `articles` table
 */
INSERT INTO articles (
	`titles`,
	`content`,
	`person_id`
) VALUES
	('article 1', 'some text', 1),
	('article 2', 'some more text' 1),
	('article 3', 'even more text', 1),
	('article 4', 'wow so much text', 1);

/**
 * Create a select statement using the LIKE keyword
 */
SELECT * FROM articles WHERE title LIKE '%article%';


/**
 * Create a select statement without using the BETWEEN keyword
 */
SELECT * FROM my_db.orders
WHERE
created_at >= '2015-09-08 14:48:00'
AND
created_at <= '2016-09-08 15:34:00';


/**
 * Create a select statement using the BETWEEN keyword
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND
'2016-09-08 15:34:00';


/**
 * Using AND multiple times in your select query.
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND
'2015-09-08 15:34:00'
AND
amount > 12.00;


/**
 * Using the NOT keyword
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND
'2015-09-08 15:34:00'
AND NOT
amount > 12.00;


/**
 * Create a select query that uses the NOT 
 * keyword with the BETWEEN keyword
 */
SELECT * FROM my_db.orders
WHERE amount
NOT BETWEEN 
13
AND
16;


/**
 * Ordering selected data
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND
'2016-09-08 15:34:00'
AND 
amount > 12.00
ORDER BY person_id;


/**
 * Order by using the DESC keyword
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND 
'2016-09-08 15:34:00'
AND amount > 12.00
ORDER BY person_id DESC;


/**
 * Using ORDER BY on the amount field
 */
SELECT * FROM my_db.orders
WHERE created_at
BETWEEN
'2015-09-08 14:48:00'
AND
'2016-09-08 15:34:00'
AND NOT
amount > 12.00
ORDER BY amount DESC;


/**
 * Create a select query using GROUP BY
 */
SELECT person_id, COUNT(amount)
FROM my_db.orders GROUP BY person_id;


/**
 * Select query using joins
 */
SELECT * FROM `my_db`.`people`
JOIN `my_db`.`profiles`
ON
people.id = profiles.person_id;


/**
 * A more complex select query using CONCAT, SUM, AS and GROUP BY
 */
SELECT CONCAT(people.first_name, ' ', people.second_name) 
AS fullname,
SUM(orders.amount) AS total_spend
FROM `my_db`.`people`
JOIN `my_db`.`orders`
ON people.id = orders.person_id
GROUP BY people.id;


/**
 * Example of a select query using LEFT joins
 */
SELECT people.first_name, orders.id
FROM my_db.people
LEFT JOIN my_db.orders
ON people.id = orders.person_id
ORDER BY people.first_name;


/**
 * Example of a select query using a RIGHT join
 */
SELECT orders.id, people.first_name
FROM my_db.orders
RIGHT JOIN my_db.people
ON orders.person_id = people.id
ORDER BY orders.person_id;
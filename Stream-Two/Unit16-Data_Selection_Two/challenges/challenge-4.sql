/**
 * Create four more orders 
 * for each person
 */
INSERT INTO `my_db`.`orders` (
	`person_id`,
	`amount`
) VALUES 
	(1, 12.04),
	(1, 13.50),
	(1, 18.00),
	(1, 2.00),
	(2, 3.04),
	(2, 3.77),
	(2, 9.89),
	(2, 10.11),
	(3, 6.07),
	(3, 12.21),
	(3, 9.09),
	(3, 14.97),
	(4, 17.99),
	(4, 13.00),
	(4, 4.81),
	(4, 7.81);

/**
 * Select all the rows from
 * the orders table where the person_id
 * is between 2 and 3
 */
SELECT * FROM my_db.orders WHERE person_id
BETWEEN 2 AND 3;
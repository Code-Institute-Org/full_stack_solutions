/**
 * Add three new people to our
 * `people` table.
 */
INSERT INTO `my_db`.`people` (
	`first_name`,
	`second_name`,
	`DOB`
) VALUES
	("Bruce", "Wayne", STR_TO_DATE("27-05-1939", "%d-%m-%Y")),
	("Barbara", "Gordon", STR_TO_DATE("03-01-1967", "%d-%m-%Y")),
	("Clark", "Kent", STR_TO_DATE("01-06-1938", "%d-%m-%Y"));

/**
 * Create three orders for each 
 * new row in the `people` table
 */
INSERT INTO `my_db`.`orders` (
	`person_id`,
	`amount`
) VALUES 
	(2, 12.34),
	(2, 10.09),
	(2, 9.99),
	(3, 5.67),
	(3, 2.90),
	(3, 7.11),
	(4, 9.01),
	(4, 10.75),
	(4, 11.11);

/**
 * SELECT DISTINCT for each of unique 
 * person_id's in the `orders` table.
 */
SELECT DISTINCT(person_id) FROM `my_db`.`orders`;
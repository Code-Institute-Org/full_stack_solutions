/**
 * Use CONCAT and SUM to retrieve a results
 * resembling the following string:
 * "Wally West spent a total of <total amount>"
 */
SELECT CONCAT("Wally West spent a total of ") AS full_name,
SUM(amount) AS total FROM `my_db`.`orders` WHERE person_id=1;
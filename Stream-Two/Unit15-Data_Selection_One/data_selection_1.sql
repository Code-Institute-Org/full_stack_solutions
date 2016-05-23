USE my_db;


/**
 * Select all columns from he `orders` table
 */
SELECT * FROM my_db.orders;


/**
 * Select specific columns from the `orders` table
 */
SELECT amount, created_at FROM my_db.orders;


/**
 * Select columns using the AS keyword to return more 
 * readable column names
 */
SELECT amount, created_at AS purchased FROM my_db.orders;


/**
 * Selecting data using the WHERE condition to filter data
 */
SELECT amount, created_at AS purchased FROM my_db.orders
WHERE person_id = 1;


/**
 * Using the COUNT function to get a total amount of orders
 * from the database
 */
SELECT COUNT(amount) FROM my_db.orders;


/**
 * Using COUNT and SUM will give the total orders for
 * a person as well as the total amounts that they have
 * ordered.
 */
SELECT COUNT(amount), SUM(amount) FROM my_db.orders
WHERE person_id = 1;


/**
 * Using the AS keyword to return more readable column names
 * for the COUNT and SUM functions
 */
SELECT COUNT(amount) AS total_sales, 
SUM(amount) AS total_amount_spent FROM my_db.orders
WHERE person_id = 1;


/**
 * Select multiple columns using CONCAT
 */
SELECT CONCAT(first_name, ',', second_name)
AS full_name FROM `my_db`.`people`;


/**
 * Using the DISTINCT keyword
 */
SELECT DISTINCT(amount) FROM my_db.orders;
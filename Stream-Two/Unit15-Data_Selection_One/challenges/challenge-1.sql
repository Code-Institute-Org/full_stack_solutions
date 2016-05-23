/**
 * Using the AVG function to calculate the
 * average_spend from the `amount` column on the
 * `orders` table
 */
SELECT AVG(amount) AS average_spend
FROM my_db.orders WHERE person_id=1;
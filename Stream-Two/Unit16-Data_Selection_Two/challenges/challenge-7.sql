/**
 * Run the query without the
 * GROUP BY
 */
SELECT person_id, COUNT(amount)
FROM my_db.orders;
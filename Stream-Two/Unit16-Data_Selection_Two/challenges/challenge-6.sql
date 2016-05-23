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
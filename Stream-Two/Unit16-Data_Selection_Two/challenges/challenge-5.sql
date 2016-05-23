/**
 * Select all rows from the `articles`
 * table where the content column starts with
 * 'some' and exclude rows where the title ends
 * with 2.
 */
SELECT * FROM articles WHERE content LIKE "some%" 
AND title NOT LIKE "%2";
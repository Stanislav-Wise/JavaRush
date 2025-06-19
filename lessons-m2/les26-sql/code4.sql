-- SELECT 
-- 	c.customer_id,
-- 	c.first_name,
-- 	c.last_name,
-- 	(SELECT COUNT(*)
-- 	 FROM rental r
-- 	 WHERE r.customer_id = c.customer_id)
-- FROM customer c;

SELECT 
	customer_id,
	first_name,
	last_name
FROM customer
WHERE customer_id IN (
	SELECT customer_id 
	FROM rental
	WHERE staff_id = 2
);
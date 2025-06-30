-- SELECT  payment_id,
-- 		customer_id,
-- 		amount,
-- 		AVG(amount) OVER (),
-- 		SUM(amount) OVER ()
-- FROM payment;


SELECT *
FROM (
	SELECT  payment_id,
			customer_id,
			amount,
			AVG(amount) OVER () AS avg_amount
	FROM payment
) t
WHERE amount > avg_amount;

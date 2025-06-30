-- SELECT  payment_id,
-- 		customer_id,
-- 		amount,
-- 		ROW_NUMBER() OVER (ORDER BY amount ASC) AS rn
-- FROM payment;


-- SELECT  payment_id,
-- 		customer_id,
-- 		payment_date,
-- 		amount,
-- 		SUM(amount) OVER (ORDER BY payment_date) AS rt
-- FROM payment;


SELECT  payment_id,
		customer_id,
		payment_date,
		amount,
		SUM(amount) OVER (
			PARTITION BY customer_id
			ORDER BY payment_date) AS rt
FROM payment;
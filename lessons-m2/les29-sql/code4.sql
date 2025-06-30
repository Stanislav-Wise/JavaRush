-- SELECT  payment_id,
-- 		customer_id,
-- 		amount,
-- 		SUM(amount) OVER (PARTITION BY customer_id) AS total_by_customer,
-- FROM payment;


SELECT  payment_id,
		customer_id,
		amount,
		AVG(amount) OVER (PARTITION BY customer_id) AS customer_avg
FROM payment;
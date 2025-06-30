-- SELECT payment_id, customer_id, amount
-- FROM payment;


SELECT  payment_id,
		customer_id,
		amount,
		SUM(amount) OVER ()
FROM payment;
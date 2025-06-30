SELECT  payment_id,
		customer_id,
		payment_date,
		amount,
		SUM(
			CASE
				WHEN customer_id = 2 THEN amount
				ELSE 0
			END
		) OVER () as cus_1_total
FROM payment;
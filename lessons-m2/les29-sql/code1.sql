-- SELECT c.customer_id, c.first_name, c.last_name, r.rental_id, r.rental_date, r.return_date
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- WHERE r.return_date - r.rental_date > INTERVAL '5 days';


WITH total_payments AS (
	SELECT c.customer_id, SUM(p.amount) AS total
	FROM customer c
	JOIN payment p ON c.customer_id = p.customer_id
	GROUP BY c.customer_id
),
	rental_counts AS (
	SELECT c.customer_id, COUNT(r.rental_id) AS rentals
	FROM customer c
	JOIN rental r ON c.customer_id = r.customer_id
	GROUP BY c.customer_id
)


SELECT c.customer_id, c.first_name, c.last_name, tp.total, rc.rentals
FROM customer c
JOIN total_payments tp ON c.customer_id = tp.customer_id
JOIN rental_counts rc ON c.customer_id = rc.customer_id;
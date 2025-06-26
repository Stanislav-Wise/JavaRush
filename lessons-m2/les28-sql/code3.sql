-- CREATE TABLE customer_copy AS
-- SELECT * FROM customer WHERE false;

-- INSERT INTO customer_copy (store_id, first_name, last_name, email, address_id, active)
-- SELECT store_id, first_name, last_name, email, address_id, active
-- FROM customer
-- WHERE store_id = 1;


-- UPDATE customer_copy
-- SET store_id = 7;


-- UPDATE customer_copy
-- SET store_id = 3, last_name = 'Petrov';


-- UPDATE customer_copy
-- SET last_name = 'Ivanov'
-- WHERE first_name LIKE 'A%';


-- DELETE FROM customer_copy
-- WHERE last_name = 'Petrov';


-- DELETE FROM customer_copy;


-- UPDATE customer_copy
-- SET last_name = 'Sidorov'
-- WHERE address_id IN (
-- 	SELECT address_id
-- 	FROM address
-- 	WHERE city_id = 3
-- );



DELETE FROM customer_copy
WHERE address_id IN (
	SELECT address_id
	FROM address
	WHERE city_id = 2
);
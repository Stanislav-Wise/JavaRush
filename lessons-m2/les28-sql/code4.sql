BEGIN;

UPDATE customer_copy
SET store_id = 11;

UPDATE customer_copy
SET last_name = 'Bobovv';


SELECT * FROM customer_copy;

ROLLBACK;
COMMIT;
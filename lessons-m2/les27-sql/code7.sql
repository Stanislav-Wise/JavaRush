-- ALTER TABLE customer_demo
-- ADD COLUMN phone TEXT;


-- ALTER TABLE customer_demo
-- ADD COLUMN is_ver BOOLEAN  DEFAULT FALSE;



-- ALTER TABLE customer_demo
-- DROP COLUMN is_ver;


-- ALTER TABLE customer_demo
-- RENAME COLUMN is_verified TO is_active;


-- ALTER TABLE customer_demo
-- ALTER COLUMN is_active TYPE VARCHAR(5);


-- ALTER TABLE customer_demo
-- ALTER COLUMN city SET DEFAULT 'Сочи';



-- ALTER TABLE customer_demo
-- ALTER COLUMN city DROP DEFAULT;



-- ALTER TABLE customer_demo
-- ADD CONSTRAINT unique_name UNIQUE (name);


-- ALTER TABLE customer_demo
-- ADD CONSTRAINT fk_name FOREIGN KEY (name) REFERENCES staff(first_name);

-- ALTER TABLE customer_demo
-- DROP CONSTRAINT unique_name;


-- ALTER TABLE customer_demo
-- RENAME TO client_demo;


DROP TABLE client_demo CASCADE;
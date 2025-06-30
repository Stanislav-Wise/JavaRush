-- CREATE FUNCTION name_fun()
-- RETURNS integer
-- AS $$

-- 	SELECT 37;

-- $$ LANGUAGE SQL;

-- SELECT name_fun();



-- CREATE FUNCTION double_number(x integer)
-- RETURNS integer
-- AS $$

-- 	SELECT x * 2;

-- $$ LANGUAGE SQL;

-- SELECT double_number(5);






-- CREATE FUNCTION get_f_n(x integer)
-- RETURNS text
-- AS $$

-- 	SELECT first_name
-- 	FROM customer
-- 	WHERE customer_id = x

-- $$ LANGUAGE SQL;

-- SELECT get_f_n(3);


-- CREATE OR REPLACE FUNCTION ...

-- DROP FUNCTION get_f_n(x integer);


 CREATE OR REPLACE FUNCTION say_hello()
 RETURNS text
 AS $$
 	SELECT 'hello world';
 $$ LANGUAGE SQL;

 SELECT say_hello();
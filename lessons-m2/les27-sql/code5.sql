CREATE TABLE customer_demo2 (
	customer_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	city TEXT DEFAULT 'Москва',
	age INTEGER CHECK(age >= 18),
	status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive'))
)

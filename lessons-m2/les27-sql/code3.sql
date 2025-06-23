CREATE TABLE review_new (
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER NOT NULL,
	customer_id INTEGER NOT NULL,
	review_text TEXT,
	rating NUMERIC(2, 1) NOT NULL,
	review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	is_active BOOLEAN DEFAULT TRUE,
	CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES film(film_id),
	CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
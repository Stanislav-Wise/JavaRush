CREATE TABLE test_table_not_pk (
	id SERIAL,
	name_id INTEGER UNIQUE,
	name TEXT NOT NULL,
	birth_day DATE,
	word CHAR(10),
	string VARCHAR(10),
	PRIMARY KEY (id, name_id),
	CONSTRAINT unique_word UNIQUE (word, string)
)
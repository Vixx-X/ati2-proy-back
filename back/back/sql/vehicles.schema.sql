CREATE TABLE vehicles (
	id SERIAL PRIMARY KEY,
	year INT NOT NULL,
	make VARCHAR(50) NULL,
	model VARCHAR(50) NOT NULL,
	UNIQUE (year, make, model)
);
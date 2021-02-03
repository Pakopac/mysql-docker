1)
SELECT * FROM offices ORDER BY country;
offices.select().order_by(offices.c.country)

SELECT * FROM offices ORDER BY state;
offices.select().order_by(offices.c.state)

SELECT * FROM offices ORDER BY city;
offices.select().order_by(offices.c.city)

2)
SELECT COUNT(*) FROM employees;
employees.count()

3)
SELECT SUM(amount) FROM payments;


"Q1 part1"
\c dvdrental
\dt dvdrental

"Q1 part2"
SELECT
first_name
FROM
customer
WHERE
first_name LIKE 'R%' or first_name  LIKE '%n'

"Q1 part3"
SELECT
COUNT (customer_id)
FROM
customer
WHERE
customer_id>20

"Q1 part4"
 SELECT
 first_name
 FROM
 actor
 WHERE
 first_name LIKE 'Nick' or first_name  LIKE 'Ed'  or first_name  LIKE 'Bette'

 "Q1 part5"
 SELECT DISTINCT
 first_name
 FROM
 actor
 ORDER BY first_name ASC

 "Q1 part6"
 SELECT
 AVG(rental_duration) as avgRate , Min(rental_duration) AS minRate,MAX(rental_duration) AS maxRate , SUM(rental_duration) as sumRate
 FROM
 film

"Q1 part7"
 SELECT
customer.customer_id, first_name, last_name, return_date, amount
FROM payment
INNER JOIN rental
ON payment.rental_id=rental.rental_id
INNER JOIN customer
ON rental.customer_id=customer.customer_id;

"Q1 part8"
SELECT
CONCAT(first_name, ' ', last_name), address, city.city_id, city, country
FROM customer
INNER JOIN address
ON customer.address_id=address.address_id
INNER JOIN city
ON address.city_id=city.city_id
ON country.country_id=city.country_id;
ORDER BY country
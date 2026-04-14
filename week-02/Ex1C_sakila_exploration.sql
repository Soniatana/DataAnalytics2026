/*
a) The actor table includes actor_id, first_name, last_name, and last_update.
b) The film table includes film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) The film_actor table contains both actor_id and film_id.
d) The rental table includes information about each rental transaction, including rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. The information is mostly easy to read because each row represents one rental, but it does not show the film title directly, so you must join to other tables (inventory and film) to know which movie was rented.
e) The inventory table includes information about each inventory item (each physical copy of a film), including inventory_id, film_id, store_id, and last_update. It shows which film each inventory item refers to and which store it belongs to.
f) To find the names of all films rented on a specific date, you would use the rental table (to filter by rental_date), the inventory table (to connect rental records to a film_id), and the film table (to get the film title). These tables are related by rental.inventory_id = inventory.inventory_id and inventory.film_id = film.film_id.
*/
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;


create database zomato_db;
use zomato_db;
create table restaurants (
	restaurant_id int primary key,
    restaurant_name VARCHAR(100),
    city VARCHAR(50),
    cuisine VARCHAR(100),
    rating FLOAT,
    average_cost_for_two INT
);

INSERT INTO restaurants
(restaurant_id, restaurant_name, city, cuisine, rating, average_cost_for_two)
VALUES
(1, 'Spice Hub', 'Ahmedabad', 'Indian', 4.5, 600),
(2, 'Pizza Palace', 'Ahmedabad', 'Italian', 4.2, 800),
(3, 'Royal Restaurant', 'Mumbai', 'North Indian', 4.0, 700),
(4, 'Food Factory', 'Delhi', 'Chinese', 4.3, 500),
(5, 'Green Garden', 'Pune', 'South Indian', 4.6, 450),
(6, 'Urban Tadka', 'Ahmedabad', 'Punjabi', 4.1, 650),
(7, 'Burger Point', 'Mumbai', 'Fast Food', 3.9, 400),
(8, 'Taste Corner', 'Delhi', 'Indian', 4.4, 550);

select * from restaurants;






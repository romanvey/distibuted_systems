DROP DATABASE IF EXISTS fly_booking_db;
DROP DATABASE IF EXISTS hotel_booking_db;
DROP DATABASE IF EXISTS account_db;


CREATE DATABASE fly_booking_db;
\c fly_booking_db;
CREATE TABLE fly_booking(
booking_id SERIAL PRIMARY KEY,
client_name TEXT,
fly_number VARCHAR(20),
from_place VARCHAR(3),
to_place VARCHAR(3),
booking_date DATE);

CREATE DATABASE hotel_booking_db;
\c hotel_booking_db;
CREATE TABLE hotel_booking(
booking_id SERIAL PRIMARY KEY,
client_name TEXT,
hotel_name TEXT,
arrival DATE,
departure DATE);

CREATE DATABASE account_db;
\c account_db;
CREATE TABLE account(
account_id SERIAL PRIMARY KEY,
client_name TEXT,
amount INT CHECK (amount >= 0));

\c postgres;

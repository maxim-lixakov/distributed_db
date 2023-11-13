CREATE TABLE Cinema
(
    cinema_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    operating_hours_start TIME NOT NULL,
    operating_hours_end TIME NOT NULL,
    contact_number VARCHAR(12) NOT NULL,
    PRIMARY KEY (cinema_id)
);

CREATE TABLE Hall
(
    hall_id INT NOT NULL,
    seating_capacity INT NOT NULL,
    cinema_id INT NOT NULL,
    PRIMARY KEY (hall_id),
    FOREIGN KEY (cinema_id) REFERENCES Cinema(cinema_id)
);

CREATE TABLE Film
(
    film_id INT NOT NULL,
    title VARCHAR(50) NOT NULL,
    duration INT NOT NULL,
    base_price FLOAT NOT NULL,
    PRIMARY KEY (film_id)
);

CREATE TABLE Customer
(
    customer_id INT NOT NULL,
    first_name VARCHAR(30),
    contact_number VARCHAR(12),
    last_name VARCHAR(30),
    email VARCHAR(50),
    PRIMARY KEY (customer_id)
);

CREATE TABLE Genre
(
    genre_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY (genre_id)
);

CREATE TABLE Seat
(
    seat_id INT NOT NULL,
    seat_number INT NOT NULL,
    `row_number` INT NOT NULL,
    class_coefficient FLOAT NOT NULL,
    hall_id INT NOT NULL,
    PRIMARY KEY (seat_id),
    FOREIGN KEY (hall_id) REFERENCES Hall(hall_id)
);

CREATE TABLE Seller
(
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30),
    seller_id INT NOT NULL,
    contact_number VARCHAR(30),
    hire_date DATE,
    salary FLOAT,
    status VARCHAR(30) NOT NULL,
    cinema_id INT NOT NULL,
    PRIMARY KEY (seller_id),
    FOREIGN KEY (cinema_id) REFERENCES Cinema(cinema_id)
);

CREATE TABLE Country
(
    name VARCHAR(30) NOT NULL,
    country_id INT NOT NULL,
    PRIMARY KEY (country_id)
);

CREATE TABLE Production_country
(
    film_id INT NOT NULL,
    country_id INT NOT NULL,
    PRIMARY KEY (film_id, country_id),
    FOREIGN KEY (film_id) REFERENCES Film(film_id),
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);

CREATE TABLE Film_genre
(
    film_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (film_id, genre_id),
    FOREIGN KEY (film_id) REFERENCES Film(film_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Showtime
(
    showtime_id INT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    hall_id INT NOT NULL,
    film_id INT NOT NULL,
	price_coefficient DOUBLE NOT NULL,
    PRIMARY KEY (showtime_id),
    FOREIGN KEY (hall_id) REFERENCES Hall(hall_id),
    FOREIGN KEY (film_id) REFERENCES Film(film_id)
);

CREATE TABLE Ticket
(
    ticket_id INT NOT NULL,
    purchase_date DATE,
    price FLOAT NOT NULL,
    status VARCHAR(30) NOT NULL,
    seller_id INT NOT NULL,
    customer_id INT NOT NULL,
    showtime_id INT NOT NULL,
    seat_id INT NOT NULL,
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (seller_id) REFERENCES Seller(seller_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (showtime_id) REFERENCES Showtime(showtime_id),
    FOREIGN KEY (seat_id) REFERENCES Seat(seat_id)
);

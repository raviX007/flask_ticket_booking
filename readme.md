# Online Movie Ticket Booking System

This is a backend API for an online movie ticket booking system, implemented using Flask and Flask-RESTful.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Models](#models)
  - [API Endpoints](#api-endpoints)
    - [Movies](#movies)
    - [Theaters](#theaters)
    - [Showtimes](#showtimes)
  - [Validations](#validations)
  - [Documentation](#documentation)
  - [Testing](#testing)
  - [Security](#security)
  - [Data Persistence](#data-persistence)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Online Movie Ticket Booking System is a backend API that allows users to browse available movies, view showtimes, reserve seats, and purchase tickets. This system is designed to provide a robust and scalable solution for movie ticket booking.

## Features

- **Movie Management**: Allows users to create, read, update, and delete movie information, including title, director, genre, release date, duration, and synopsis.
- **Theater Management**: Allows users to create, read, update, and delete theater information, including name, location, and capacity.
- **Showtime Management**: Allows users to create, read, update, and delete showtime information, including movie, theater, date and time, and available seats.
- **Seat Reservation**: Allows users to check the available seats for a specific showtime and reserve seats.
- **Validation**: Ensures that showtime date and time are in the future and implements other necessary validations.
- **Documentation**: Provides detailed documentation of the API endpoints using Swagger or equivalent tools.
- **Testing**: Includes unit tests to ensure the correctness of the API endpoints and error handling.
- **Security**: Implements appropriate security measures to prevent unauthorized access to the API, including authentication and authorization mechanisms.
- **Data Persistence**: Uses a relational database (e.g., SQLite, MySQL, PostgreSQL) to persist movie, theater, and showtime data, with the help of an ORM (Object-Relational Mapping) library.

## Installation

To run the Online Movie Ticket Booking System, follow these steps:

1. Clone the repository:

```
 git clone https://github.com/your-username/online-movie-ticket-booking-system.git
```

2. Change to the project directory:

```
 cd online-movie-ticket-booking-system
```


3. Create a virtual environment (optional, but recommended):

```
 python -m venv venv
 source venv/bin/activate  
 use venv\Scripts\activate for windows
```


4. Install the required dependencies:

```
 pip install -r requirements.txt
```


5. Run the application:

```
 python app.py
```

The API will be available at `http://localhost:5000`.

## Usage

### Models

The system has the following models:

1. **Movie**:
- `title`: The title of the movie.
- `director`: The director of the movie.
- `genre`: The genre of the movie.
- `release_date`: The release date of the movie.
- `duration`: The duration of the movie in minutes.
- `synopsis`: A brief synopsis of the movie.

2. **Theater**:
- `name`: The name of the theater.
- `location`: The location of the theater.
- `capacity`: The capacity of the theater.

3. **Showtime**:
- `movie`: The movie associated with the showtime (foreign key).
- `theater`: The theater where the showtime is held (foreign key).
- `date_time`: The date and time of the showtime.
- `available_seats`: The number of available seats for the showtime.

### API Endpoints

The system provides the following API endpoints:

#### Movies

- `GET /movies`: List all movies.
- `GET /movies/<int:movie_id>`: Retrieve a specific movie.
- `POST /movies`: Create a new movie.
- `PUT /movies/<int:movie_id>`: Update an existing movie.
- `DELETE /movies/<int:movie_id>`: Delete a movie.

#### Theaters

- `GET /theaters`: List all theaters.
- `GET /theaters/<int:theater_id>`: Retrieve a specific theater.
- `POST /theaters`: Create a new theater.
- `PUT /theaters/<int:theater_id>`: Update an existing theater.
- `DELETE /theaters/<int:theater_id>`: Delete a theater.

#### Showtimes

- `GET /showtimes`: List all showtimes.
- `GET /showtimes/<int:showtime_id>`: Retrieve a specific showtime.
- `POST /showtimes`: Create a new showtime.
- `PUT /showtimes/<int:showtime_id>`: Update an existing showtime.
- `DELETE /showtimes/<int:showtime_id>`: Delete a showtime.
- `GET /showtimes/<int:showtime_id>/available_seats`: Get the available seats for a specific showtime.
- `POST /showtimes/<int:showtime_id>/reserve_seats`: Reserve seats for a specific showtime.

### Validations

The system includes the following validations:

- Ensure that the showtime date and time are in the future.
- Implement other necessary validations as per your discretion.

### Data Persistence

The system uses a relational database (e.g., SQLite, MySQL, PostgreSQL) to persist movie, theater, and showtime data. An ORM (Object-Relational Mapping) library is used for database operations, and raw SQL queries are avoided.

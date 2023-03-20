# Test Task: Employee Management System

This is a test task for an Employee Management System built with Python, aiohttp, and SQLAlchemy.

## Task description

Создайте веб страницу, которая будет выводить иерархию сотрудников в древовидной форме.

- Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные:
   - ФИО;
   - Должность;
   - Дата приема на работу;
   - Размер заработной платы;
- У каждого сотрудника есть 1 начальник;
- Возможность добавлять/редактировать сотрудника;
- Не забудьте отобразить должность сотрудника.

### Технические требования:
- Python 3.9+
- aiohttp 3.8+
- PostgreSQL 10+

### Будет плюсом:
- Использование docker и docker-compose для поднятия и развертывания dev-среды.


## Instructions

### Running the containers

1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).
2. Clone the repository.
3. In the project folder, run `docker-compose --env-file env/.env up --build`.

The application should now be running at http://0.0.0.0:8080/employee.

### Applying migrations

To apply migrations, execute the following command in the project folder:

`docker-compose exec app alembic upgrade head`


### Creating test data

To run script that adds list of test employees, execute the following command in the project folder:

`docker-compose exec app python3 app/scripts/create_test_data.py`


## Documentation

The application consists of several main components:

- `app`: The main application folder, which contains the following:
  - `migrations`: Contains the Alembic migration files.
  - `scripts`: Contains the initial test data.
  - `models`: Contains the SQLAlchemy model for the Employee.
  - `routes`: Contains the routing configuration for the application.
  - `schemas`: Contains the Pydantic schemas for validation.
  - `views`: Contains the view functions for handling requests.
  - `templates`: Contains the Jinja2 templates for the application.
  - `main.py`: The entry point of the application. It initializes the application, sets up Jinja2 for template rendering, and registers the startup function to create the database. It also sets up the routes for the application and runs the web server.
  - `db_connection.py`: Contains the database connection configuration and a utility function to create an asynchronous session with the database using SQLAlchemy. It also initializes the database with the defined schema.
  - `router.py`: A file that organizes the routes for the application. It imports and sets up the employee-related routes.
  - `utils.py`: Contains utility functions, such as the serialize_employee function, which serializes an employee object to a dictionary with a configurable depth for subordinates.
- `tests`: Contains the test files for the application.
- `Dockerfile`: The Dockerfile for building the application container.
- `docker-compose.yml`: The Docker Compose configuration for running the application and the database.

## API Endpoints

The application provides the following API endpoints:

- `GET /employee`: Retrieve a list of all employees.
- `POST /employee`: Create a new employee. The request body should be a JSON object containing the following fields:
  - `full_name`: The full name of the employee (required, 3-100 characters).
  - `position`: The position of the employee (required, 2-100 characters).
  - `hire_date`: The date of employment in the format "YYYY-MM-DD" (required).
  - `salary`: The salary of the employee (required, greater than 0).
  - `supervisor_id`: The ID of the employee's supervisor (optional, greater than 0).
- `POST /employee/{id}`: Update an existing employee by ID. The request body should be a JSON object containing the same fields as for the `POST /employee` endpoint.
- `POST /employee/{id}`: Delete an employee by ID.

To interact with the API, you can use tools like [curl](https://curl.se/) or [Postman](https://www.postman.com/), or you can build a frontend application that sends requests to the API.

# Pizza Delivery API

This project is a Django REST API that allows users to sign up, log in, place pizza orders, and manage orders. It includes token-based authentication using JWT and role-based access for specific operations.

## Features

- **User Authentication**: Sign up, log in, and manage authentication with JWT.
- **Order Management**: Place, update, and delete pizza orders.
- **Role-based Access**: Superusers have additional privileges to view and update order statuses.
- **JWT Token Refresh and Verification**: Allows refreshing tokens and verifying their validity.

## API Endpoints

### Authentication

| METHOD | ROUTE               | FUNCTIONALITY                     | ACCESS     |
|--------|---------------------|------------------------------------|------------|
| POST   | `/auth/signup/`      | Register a new user               | All users  |
| POST   | `/auth/jwt/create/`  | Log in a user                     | All users  |
| POST   | `/auth/jwt/refresh/` | Refresh the access token          | All users  |
| POST   | `/auth/jwt/verify/`  | Verify the validity of a token     | All users  |

### Order Management

| METHOD | ROUTE                              | FUNCTIONALITY                         | ACCESS     |
|--------|------------------------------------|----------------------------------------|------------|
| POST   | `/orders/`                         | Place an order                        | All users  |
| GET    | `/orders/`                         | Get all orders                        | All users  |
| GET    | `/order/{order_id}/`               | Retrieve an order                     | Superuser  |
| PUT    | `/orders/{order_id}/`              | Update an order                       | All users  |
| PUT    | `/orders/update-status/{order_id}/`| Update the status of an order         | Superuser  |
| DELETE | `/delete/{order_id}/`              | Delete/Remove an order                | All users  |
| GET    | `/orders/user/{user_id}/orders/`   | Get a user's orders                   | All users  |
| GET    | `/orders/user/{user_id}/order/{order_id}/`| Get a user's specific order    | All users  |

## How to Run the Project

### Clone the repository:

```bash
git clone https://github.com/meetvivek/PizzaOrder-API-Django.git
cd PizzaOrder-API-Django
```
### Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### Install the required packages:
```bash
pip install -r requirements.txt
```

### Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```


### Create a superuser to access the Django admin panel (optional):
```bash
python manage.py createsuperuser
```

### Run the development server:
```bash
python manage.py runserver
```

### Open the API in your browser or Postman at:
```bash
http://127.0.0.1:8000/
```
## Testing the API in Postman
- Use the routes provided in the API Endpoints section to test the API - functionality in Postman.
- Be sure to include the JWT token in the headers for routes that require authentication.

## Tools and Technologies
- **Django**: Backend framework
- **Django REST Framework**: For building APIs
- **JWT (JSON Web Tokens)**: For user authentication
- **PostgreSQL (or SQLite)**: As the database
- **Postman**: For API testing

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

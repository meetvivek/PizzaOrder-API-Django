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


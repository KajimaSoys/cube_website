# README for CubeKazan Website Repository

## Introduction
Welcome to the GitHub repository for the CubeKazan website! CubeKazan is a leading provider of cardboard boxes in Kazan, offering a wide range of packaging solutions to meet diverse needs. This repository hosts the source code for our official website, https://cubekazan.ru.

## Technology Stack
- **Frontend**: Vue.js
- **Backend**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker (Compose)
- **Web Servers**: Nginx
- **Programming Language**: Python, JavaScript

## Features
- **Product Catalog**: Browse through our extensive range of cardboard box products.
- **Custom Orders**: Place orders for custom-sized boxes.
- **E-Commerce Integration**: An integrated shopping cart and checkout system.
- **Admin Panel**: For managing products, orders, and customer information.
- **Responsive Design**: Ensures a seamless experience across various devices.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```shell
   git clone https://github.com/KajimaSoys/cube_website.git
   ```
2. Navigate to the project directory.
3. Before building and running the containers, ensure to configure the `.env` files for both backend and frontend. Set the values for the following variables:
   - **Backend `.env`**:
     - `DEBUG` - Set to `True` for development.
     - `SECRET_KEY` - A Django secret key.
     - `ALLOWED_HOSTS` - Default is `127.0.0.1,localhost`.
     - `DB_NAME` - PostgreSQL database name.
     - `DB_USER` - PostgreSQL database user.
     - `DB_PASSWORD` - PostgreSQL database password.
     - `DB_HOST` - Database host, default is `db`.
     - `DB_PORT` - Database port, default is `5432`.
     - `HMAC_KEY` - Key for HMAC.
     - `CSRF_COOKIE_SECURE` - Set to `True` for HTTPS.
     - `SESSION_COOKIE_SECURE` - Set to `True` for HTTPS.
     - `SMSRU_APIKEY` - (Optional) API key for sms.ru.
     - `SMSRU_CLIENT` - (Optional) Your number to receive messages from sms.ru.
   - **Frontend `./client/.env`**:
     - `VITE_BACKEND_HOST` - Backend host, default is `http://127.0.0.1:8000`.
     - `VITE_FRONTEND_HOST` - Frontend host, default is `http://localhost:5173`.
     - `VITE_HMAC_SECRET_KEY` - HMAC secret key for frontend.

   Note: For empty values in the `.env` files, input the necessary details. For pre-filled values, you can use them as-is or modify them according to your setup requirements.

4. Use Docker Compose to build and run the containers:
   ```shell
   docker compose build
   ```
   ```shell
   docker compose up -d
   ```
5. Access the application at `localhost` or the configured port.

## License
This project is licensed under the [MIT License](LICENSE).

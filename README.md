# YaYa Wallet Webhook Project

This project implements a webhook endpoint to receive and process transaction notifications for YaYa Wallet. The application is built using Python and Django, with Docker for containerization and PostgreSQL for storing the payloads.
To get started, clone the project repository from GitHub:
Setting Up the Project with Docker

    Install Docker and Docker Compose if you haven't already. Follow the installation instructions for your operating system from the Docker website and Docker Compose documentation.

    Build and Start the Docker Containers:

    bash

sudo docker-compose up --build

This command will build the Docker images and start the web and database services.

Run Database Migrations:

After the containers are up, run the following command to apply any database migrations:

bash

    sudo docker-compose run web python manage.py migrate

Registering the Webhook

To test the webhook endpoint, you can use Postman or any other API testing tool:

    Open Postman.

    Create a new POST request to the following URL:

    ruby

http://0.0.0.0:8000/webhooks/transaction/

Set the request body to JSON format and include the payload you want to send. Here's an example:

json


Send the request.


Testing the Solution

To test the solution:

    Ensure that the Docker containers are running and the database is properly set up.
    Use Postman to send test webhook requests to the endpoint.
    Verify that the payloads are correctly stored in the PostgreSQL database.

Conclusion

This project demonstrates a complete solution for processing webhook notifications for YaYa Wallet. The code is structured for maintainability and clarity, allowing for easy future enhancements.
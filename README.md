# PROPERTY LISTINGS

This project automate backgound email by adding **Celery with RabbitMQ** for background task management and implementing **email notifications** for bookings.

## Features

- Configured **Celery** with RabbitMQ as the message broker.
- Added a background task to send **booking confirmation emails**.
- Integrated Celery with Django using a `celery.py` file and updated `settings.py`.
- Triggered email notifications asynchronously when a booking is created.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/brytebee/alx-backend-caching_property_listings.git
   cd alx-backend-caching_property_listings
   ```

2. Start RabbitMQ (make sure it’s installed and running).

3. Run Celery worker:

   ```bash
   celery -A alx-backend-caching_property_listings worker --loglevel=info
   ```

4. Run Django server:

   ```bash
   python manage.py runserver
   ```

## Testing

- Create a new booking via the API.
- A **confirmation email** will be sent asynchronously using Celery.

# Rocko-Deploy
The Registration Portal for Alcheringa-The annual cultural fest of IIT Guwahati's Rock band competition,
 where the participating teams have to register themselves.
## Project-setup

1. Clone the repository:

git clone https://github.com/Kruthikesh/rocko-deploy

2. Navigate to the project directory.

3. pip install psycopg2 

   pip install phonenumbers

4. Apply database migrations:

python manage.py makemigrations

python manage.py migrate

5. Start the development server:

python manage.py runserver

6. Open your web browser and visit `http://localhost:8000` to access Rocko-Portal.

## Dependencies

AudioVize has the following dependencies:

- Django: A high-level Python web framework for rapid development.

- Django templates: Used to create HTML templates for rendering views.

- SQLite: A lightweight, file-based database used as the default database backend in Django.



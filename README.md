# 🌟 Django API Project 🌟
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## Overview
This project is a Django API, built using Python and Django framework. It provides a basic structure for building APIs, including models, serializers, views, and URLs.

## Key Features
* 📝 **Models**: Defines the structure of the data stored in the database.
* 📊 **Serializers**: Handles the conversion of data between the database and the API.
* 📈 **Views**: Handles HTTP requests and returns HTTP responses.
* 📁 **URLs**: Maps URLs to views.

## Technology Stack
* Backend: Django
* Database: SQLite
* Libs: Django Rest Framework

## Getting Started
To get started with this project, follow these steps:
1. Clone the repository: `git clone https://github.com/Rohitw3code/django-api.git`
2. Navigate to the project directory: `cd django-api`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Usage
To interact with the API, use a tool like curl or a REST client. The API endpoints are defined in the `urls.py` file.

## Configuration
No specific configuration is required for this project. However, you may need to configure the database settings in the `settings.py` file.

## Contributing
Contributions are welcome! To contribute, fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Project Structure
The project structure is as follows:
```markdown
django-api/
|-- api/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- companyapi/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
|-- README.md
```
## Credit to
Built with ❤️ by Rohitw3code
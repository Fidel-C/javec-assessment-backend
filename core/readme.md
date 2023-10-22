# Django Contact Manager

## Overview

This is a Django project that serves as a contact manager application. It is built using the Django REST framework and includes two apps: "accounts" for authentication and "contacts" for managing user contact information. 

## Prerequisites

Before you get started, make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Django REST framework](https://www.django-rest-framework.org/#installation)
- [django-simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/installation.html)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/django-contact-manager.git
   ```

2. Change your working directory to the project folder:

   ```bash
   cd django-contact-manager
   ```

3. Install the project's dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a Django superuser to manage the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Usage

To run the application, use the following command:

```bash
python manage.py runserver
```

The development server will start, and you can access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Apps

### 1. Accounts

The "accounts" app handles user authentication. You can register new users, log in, and manage user accounts.

### 2. Contacts

The "contacts" app is responsible for managing user contact information. It provides CRUD (Create, Read, Update, Delete) functionality for contacts.

## API Endpoints

This project provides the following API endpoints:

- `/accounts/` - User registration and management.
- `/contacts/` - CRUD operations for managing user contacts.

## Authentication

This project uses [django-simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for JWT (JSON Web Token) authentication. You need to obtain a JWT token by authenticating through the `/accounts/token/` endpoint to access protected endpoints.

## Contributing

Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Your contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE). Please review the license before using or distributing this code.

---

Enjoy using the Django Contact Manager! If you have any questions or need further assistance, feel free to reach out to me.
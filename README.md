# Django REST API

This repository contains a basic implementation of a REST API using the Django and Django REST Framework in Python. The API is built around a `Customer` model, which includes fields for `first_name`, `last_name`, and `date_of_birth`.

## Author

- **Phumlani Mabophe** - [phumlanimabophe](https://github.com/phumlanimabophe)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-rest-api.git
    ```

2. Navigate into the project directory:
    ```bash
    cd django-rest-api
    ```

3. Create a new virtual environment using Python 3.8:
    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:
    - On Windows, run: `env\Scripts\activate`
    - On Unix or MacOS, run: `source env/bin/activate`

5. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Apply the migrations to create the necessary database schema:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## Important Note for Maintainers

Please do not remove the `rest_framework` from the main project folder. It is a crucial part of our project infrastructure. Always ensure that it is up-to-date with the latest stable version. Regular updates are essential for the security and stability of our project. 

To update `rest_framework`, you can use the following command:

```bash
pip install -U djangorestframework

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building APIs

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
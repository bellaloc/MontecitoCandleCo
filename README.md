# Montecito Candle Company

Montecito Candle Company is a Django-based web application for managing and selling candles. This project provides a foundation for an online store where users can browse, view, and purchase candles.

#view deployed site at: https://hidden-wildwood-77572-0b9fbacc5ca7.herokuapp.com/ 

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running the Development Server](#running-the-development-server)
  - [Creating a Superuser](#creating-a-superuser)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

  
   git clone https://github.com/your-username/MontecitoCandleCo.git
   cd MontecitoCandleCo (go to the path where manage.py is located)

Create and activate a virtual environment:

bash:
python -m venv venv
or: pip install virtualenv

bash:
virtualenv venv

source venv/bin/activate  # On Unix/Mac
# or
venv\Scripts\activate  # On Windows

Install dependencies:

bash:
pip install -r requirements.txt

Apply database migrations:

bash:
python manage.py migrate

# Project Structure
montecito_candle_company/: Django project settings and configuration.
store/: Django app for managing products, orders, and related functionality.
templates/: HTML templates for rendering views.
static/: Static files such as CSS, JavaScript, and images.

# Usage
Running the Development Server

bash:
python manage.py runserver


Access the development server at http://127.0.0.1:8000/

Creating a Superuser
To access the Django admin interface, create a superuser:

bash: 
python manage.py createsuperuser

Follow the prompts to set a username, email, and password.

# Contributing
If you'd like to contribute, please fork the repository and create a pull request. Issues and feature requests are welcome!

# License
This project is licensed under the MIT License - see the LICENSE file for details.







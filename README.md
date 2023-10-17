# E-commerce

This is a basic e-commerce website built using Django, offering a range of features including:

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

### User Management

* User registration and authentication.User registration and authentication.
* User login and logout functionality.
* User profile page displaying user information.

### Product Management

* Listing of products with details like name, price, and description.
* Ability to add new products.
* Editing product details.

### Product Reviews

* Allow users to leave product reviews.
* Comments and ratings for products.

### Cart Management

* Adding products to the shopping cart.
* Viewing and editing the cart.
* Removing items from the cart.
* Calculating the total cart cost.

### Order Management

* Viewing order history with details of past purchases.
* Order details, including product names, quantities, and prices

### Payment Integration

* Integration with PayPal for seamless and secure payments.
* Payment processing for product purchases.

## Usage

1. Clone the repository to your local machine:

```git clone https://github.com/nydtab001/django-ecommerce.git```

2. Navigate to the project directory and install project dependencies using the following command:

```pip install -r requirements.txt```

3. Create the necessary database tables by making migrations:

```python manage.py makemigrations```

4. Apply the migrations to the database:

```python manage.py migrate```

6. Start the development server:

```python manage.py runserver```

7. Open your web browser and access the website at http://localhost:8000 to explore the e-commerce platform.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Commit your changes and push them to your forked repository.
6. Submit a pull request.
=======
>>>>>>> origin/master
# Sales Web Application: Back-End

This is a REST API built with Django REST Framework.

Visit this [blog post](http://krishel.com/sales_web_application) for more details.

The front-end client is available at https://github.com/krishl/sales-front.

## Installation
1. Clone or download this repository.
2. Navigate to the folder in your Terminal and run the following

```
pip3 install virtualenv
cd backend
virtualenv venv -p python3
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
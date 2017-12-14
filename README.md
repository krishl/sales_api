# Sales Web Application

This is a REST API build with Django Rest Framework.

Visit this [blog post](http://krishel.com/sales_web_application) for more details.

## Installation
1. Clone or download this repository.
2. Navigate to the folder in your Terminal and run the following

```
pip3 install virtualenv
cd backend
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
3. Navigate to the resulting URL on your preferred internet browser.
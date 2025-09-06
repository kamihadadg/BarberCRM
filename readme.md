<!-- --  


# نصب Django و Django REST Framework
pip install django djangorestframework
      pip freeze > requirements.txt 

rm db.sqlite3   # در Git Bash / Linux / Mac
del db.sqlite3  # در CMD ویندوز

rm accounts/migrations/0*.py
rm customers/migrations/0*.py
rm services/migrations/0*.py
rm appointments/migrations/0*.py

KT OK
-->

python -m venv venv

venv\Scripts\activate

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py makemigrations accounts customers services appointments

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

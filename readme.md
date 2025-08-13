
 'd:/GitPrj/Barber/venv/Scripts/activate.bat'


del db.sqlite3 
rm accounts/migrations/0*.py
rm customers/migrations/0*.py
rm services/migrations/0*.py
rm appointments/migrations/0*.py



python manage.py makemigrations accounts customers services appointments
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
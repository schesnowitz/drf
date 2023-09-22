python3 -m venv .venv
pip install django djangorestframework
django-admin createproject name
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
manage.py makemigrations booze
python manage.py migrate
git switch -c <new_branch> 
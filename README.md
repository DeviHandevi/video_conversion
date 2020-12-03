# Install Django App
Run `pipenv shell`
Install Django `pipenv install django`
Start Django Project `django-admin startproject video_converter`
Change directory `cd video_converter`
Apply the migrations for project app(s) `python manage.py migrate`
Run Project `python manage.py runserver`
Start app `python manage.py startapp video_converter_app`
Create superuser `python manage.py createsuperuser` (admin, admin)
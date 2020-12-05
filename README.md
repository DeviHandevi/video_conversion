# Install Django App
Run `pipenv shell`
Install Django `pipenv install django`
Install Django REST Framework `pipenv install djangorestframework`
Start Django Project `django-admin startproject video_converter`
Change directory `cd video_converter`
Apply the migrations for project app(s) `python manage.py migrate`
Run Project `python manage.py runserver`
Start app `python manage.py startapp video_converter_app`
Create superuser `python manage.py createsuperuser` (admin, admin)

# Install FFMPEG
Download ffmpeg from `https://ffmpeg.org/download.html#build-windows`
Add `ffmpeg\bin` to environment variable path
Try convert using cli command `ffmpeg -i input.mp4 output.webm`

# Install ffmpeg-python
Install `pipenv install ffmpeg-python`
Install `pipenv install numpy`
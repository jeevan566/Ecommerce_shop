FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=ecommerce.settings 

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py migrate --noinput

RUN python manage.py shell -c "from django.contrib.auth.models import User; \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

CMD ["bash", "-lc", "gunicorn ecommerce.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"]

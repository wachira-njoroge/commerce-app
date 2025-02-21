FROM python:3.13.2
RUN mkdir /sellerapp
WORKDIR /sellerapp
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt /sellerapp/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /sellerapp/
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8050

CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
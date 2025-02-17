FROM python:3.13.2
RUN mkdir /sellerapp
WORKDIR /sellerapp
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip freeze | tee requirements.txt && mv requirements.txt /sellerapp/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /sellerapp/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
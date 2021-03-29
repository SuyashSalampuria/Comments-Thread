# comments

comments is an application to create messages and its replies in form of threads

# Dependecies

* python3
* pip
* virtualenv

# Build and Run

1. Clone the Repository

```shell
git clone https://github.com/SuyashSalampuria/Comments-Thread
cd Comments-Thread
```

2.Make virtual environment setup

```shell
virtualenv .venv
```

3.Activate your environment

```shell
source .venv/bin/activate
```

4.Install requirements

```shell
pip install -r requirement.txt
```

5.Create a MySql database named threads. Navigate to ```/threads``` and create a file .env and store the following credentials inside it

```
SECRET_KEY=your-secret-key

DATABASE_USER=mysql-database-username
DATABASE_PASSWORD=mysql-database-password
```
5.Migrate Files

```shell
python manage.py makemigrations
python manage.py migrate
```

6.Make a Superuser

```shell
python manage.py createsuperuser
```


Press Ctrl-D

8.Run the app(on localhost:8000)

```shell
python manage.py runserver
```

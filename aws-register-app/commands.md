su: admin/admin

settings.py: 
SECRET_KEY --> Env Variable
DEBUG=False --> Env Variable

#TO collect static files and moved to a folder

python manage.py collectstatic

create a virtual environment

python -m venv venv-dev

windows: <porject_dir>: 
    venv-dev\Scripts\activate


python -m pip freeze > requirements.txt
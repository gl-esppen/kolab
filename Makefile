install:
	pip install -r requirements.txt
	python kolab/manage.py migrate
	python kolab/manage.py createsuperuser
	python kolab/manage.py collectstatic

migrations:
	python kolab/manage.py makemigrations
	python kolab/manage.py migrate


test:
	python kolab/manage.py test api


user:
	python kolab/manage.py createsuperuser

run:
	python kolab/manage.py runserver
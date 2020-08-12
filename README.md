## Reference Link ##
- [Django 2.2](https://docs.djangoproject.com/en/2.2/)
- [Requests](https://requests.readthedocs.io/en/master/user/quickstart/)

## Environment ##
* Python 3.7
* Django 2.2
* PostgreSQL 11
* Rest-framework

## Initital Data ##
* Dump data
```
python manage.py dumpdata location.province --indent 2 > _data/fixtures/initial_provinces.json
python manage.py dumpdata location.district --indent 2 > _data/fixtures/initial_districts.json
python manage.py dumpdata product.category --indent 2 > _data/fixtures/initial_categories.json
python manage.py dumpdata product.attribute --indent 2 > _data/fixtures/initial_attributes.json
python manage.py dumpdata product.attributeitem --indent 2 > _data/fixtures/initial_attribute_items.json
python manage.py dumpdata sitesetting.unit --indent 2 > _data/fixtures/initial_units.json
python manage.py dumpdata crawler.domain --indent 2 > _data/fixtures/initial_crawler_domains.json
python manage.py dumpdata crawler.link --indent 2 > _data/fixtures/initial_crawler_links.json
```
* Initial Data
```
python manage.py loaddata _data/fixtures/initial_provinces.json
python manage.py loaddata _data/fixtures/initial_districts.json
python manage.py loaddata _data/fixtures/initial_categories.json
python manage.py loaddata _data/fixtures/initial_attributes.json
python manage.py loaddata _data/fixtures/initial_attribute_items.json
python manage.py loaddata _data/fixtures/initial_units.json
```

## Development Installation ##
* Install python packages
```
python3 -m venv env
source env/bin/activate
cd map
pip install -r requirements.txt
```
* Install new python package
```
pip install <package_name>
```

* Export python packages
```
pip freeze > requirements.txt
```

* Create migration files
```
python manage.py makemigrations <module>
```

* Migrate database
```
python manage.py migrate
```

* Start project
```
python manage.py runserver
```

* Start celery work & beat
```
PORT=8200 uwsgi management/wsgi/uwsgi.ini &

celery -A map worker -l info
celery -A map beat -l info
```

* Kill celery work & beat
```
ps -aux | grep uwsgi  | awk '{print $2}'
sudo kill -9 `ps -aux | grep uwsgi  | awk '{print $2}'`

ps -aux | grep celery  | awk '{print $2}'
sudo kill -9 `ps -aux | grep celery  | awk '{print $2}'`

ps -aux | grep pyppeteer  | awk '{print $2}'
sudo kill -9 `ps -aux | grep pyppeteer  | awk '{print $2}'`
```

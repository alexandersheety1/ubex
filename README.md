test_uber - пример приложения

Установка:

1. Установить витруальное окружение
2. pip install -r requirements.txt
3. python setup.py install
4. добавить в INSTALLED_APPS файла settings.py 'ubex.apps.ubex_config'
5. python manage.py makemigrations
6. python manage.py migrate
7. Запустить приложение


--------------------------------------------------------------------

API:

Получение списка записей

method: GET

url: /имя_модели/

params:

Все поля модели, пример id=1

Сортировка, пример ordering=-id

Лимитизация, пример limit=2

--------------------------------------------------------------------------

Добавление записи:

method: POST

url: /имя_модели/

----------------------------------------------------------------------------

Получение и изменение и удаление записи по id:

method: GET, PUT, DELETE

url: /имя_модели/id/

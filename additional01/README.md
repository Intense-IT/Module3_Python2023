# SQLAlchemy и Alembic

## SQLAlchemy
Библиотека на ЯП Python для работы с базами данных посредством ORM.
### Установка
```sh
pip install sqlalchemy
```

### Применение
Используется отдельный файл (в нашем случае db.py) для настройки SQLAlchemy и создания необходимых классов.

Содержимое файла
- Настройка движка SQLAlchemy с указанием типа БД
```python
engine = create_engine(DATABASE_URL)
```
- Создание фабрики подключений
```python
Session = sessionmaker(bing=engine)
```
- Создание объекта подключения
```python
session = Session()
```
- Создание базового класса для моделей, к которым применяется ORM
```python
Base = declarative_base()
```
- Функция, создающая по хранимым в классе Base метаданным таблиц базу данных:
```python
def init_db():
    import alch_app.modeles
    Base.metadata.create_all(bind=engine)
```
Вызвать функцию можно в терминале python.

Теперь можно импортировать объект подключения session в основной файл приложения и через него выполнять все ORM-запросы.
```python
user = session.execute(select(User).filter_by(username='example')).scalar_one()
```


## Alembic
Инструмент для миграций БД.

### Установка
```sh
pip install alembic
```

### Применение
1. Инициализация миграций
    - В проекте создается папка для хранения миграций (напр., migrations)
    - Alembic инициализируется в этой папке посредством команды:
    ```sh
    alembic init migrations
    ```
2. Создание скрипта начальной миграции
    - Предварительно необходимо отредактировать два файла, alemibc.ini и env.py:
        - Изменить строку 63 для указания файла БД и ее типа:
        ```python
        sqlalchemy.url = sqlite:///my_database.db
        ```
        - Заменить строки 19-20 на ваши значения:
        ```python
        from alch_app import db
        target_metadata = db.Base.metadata
        ```
    - Генерация начальной миграции:
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```
3. Применение миграции к БД
```sh
alembic upgrade head
```

### Дополнительные команды
- Создание новых миграций
```sh
alembic revision --autogenerate -m "Migration comment"
```
- Применение конкретной миграции (указывается ее имя)
```sh
alembic upgrade version_name
```
- Откат к предыдущей версии БД
```sh
alembic downgrade -1
```
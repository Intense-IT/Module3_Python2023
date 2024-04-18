# SQLAlchemy и Alembic

## SQLAlchemy
Библиотека на ЯП Python для работы с базами данных посредством ORM.
### Установка
`pip install sqlalchemy`

### Применение
Создается отдельный файл (в нашем случае db.py) для настройки SQLAlchemy и создания необходимых классов.
Содержимое файла
Настройка движка SQLAlchemy с указанием типа БД
`engine = create_engine(DATABASE_URL)`
Создание фабрики подключений
`Session = sessionmaker(bing=engine)`
Создание объекта подключения
`session = Session()`
Создание базового класса для моделей, к которым применяется ORM
`Base = declarative_base()`

В самом конце описывается функция, создающая по хранимым в классе Base метаданным таблиц базу данных:
`def init_db():`
    `import alch_app.modeles`
    `Base.metadata.create_all(bind=engine)`

Теперь можно импортировать объект подключения session в основной файл приложения и через него выполнять все ORM-запросы.
`user = session.execute(select(User).filter_by(username='example')).scalar_one()`


## Alembic
Инструмент для миграций БД.

### Установка
`pip install alembic`

### Применение
1. Инициализация миграций
    - В проекте создается папка для хранения миграций (напр., migrations)
    - Alembic инициализируется в этой папке посредством команды:
    `alembic init migrations`
2. Создание скрипта начальной миграции
    - Предварительно необходимо отредактировать два файла, alemibc.ini и env.py:
        - Изменить строку 63 для указания файла БД и ее типа:
        `sqlalchemy.url = sqlite:///my_database.db`
        - Заменить строки 19-20 на ваши значения:
        `from alch_app import db`
        `target_metadata = db.Base.metadata`
    - Генерация начальной миграции:
    `alembic revision --autogenerate -m "Initial migration"`
3. Применение миграции к БД
`alembic upgrade head`

### Дополнительные команды
- Создание новых миграций
`alembic revision --autogenerate -m "Migration comment"`
- Применение конкретной миграции (указывается ее имя)
`alembic upgrade version_name`
- Откат к предыдущей версии БД
`alembic downgrade -1`
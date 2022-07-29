# YaMDb

[Описание](#описание) /
[История изменений](#история-изменений) /
[Развернуть локально](#развернуть-локально) /
[Документация](#документация)


## Описание
Проект [YaMDb](https://github.com/avtorsky/api_yamdb) собирает отзывы пользователей на произведения. В этом репозитории бэкенд проекта (приложение reviews) и API для него (приложение api), разработанные командой авторов:

* <a href="https://github.com/slavspart" target="_blank">slavspart</a>
* <a href="https://github.com/oitczvovich" target="_blank">oitczvovich</a>
* <a href="https://github.com/avtorsky" target="_blank">avtorsky</a>

## История изменений
Release 20220729:
* fix(./nginx/default.conf): отключена передача версии nginx на страницы ошибок

Release 20220726:
* ci(./docker-compose.yaml): настройка пайплайна сборки проекта
* ci: переключение конфига БД с SQLite на PostgreSQL
* fix(./api_yamdb/settings.py): улучшения безопастности

Release 20220706:
* fix(./api_yamdb/api/): поправлен линтинг в сериализаторах, вьюсеты CategoryViewSet и GenreViewSet переписаны согласно принципу DRY 
* fix(./api_yamdb/api_yamdb/): минорные изменения в конфиге settings.py
* fix(./api_yamdb/reviews/models.py): внесены правки в модели Comment и Review

Release 20220704:
* fix(./api_yamdb/): внесены правки в приложения api и reviews по результатам code reivew

Release 20220630:
* feat(./api_yamdb/api/filters.py): поддержана кастомная логика фильтрации объектов для эндпойнта api/v1/titles/
* fix(./api_yamdb/api/): выполнена отладка компонентов приложения api по unit-тестам

Release 20220628:
* feat(./api_yamdb/api/): подготовлены вьюсеты и сериализаторы моделей Category, Comment, Genre, Review, Title, User
* feat(./api_yamdb/api/urls.py): настроен роутинг для всех эндпойнтов API

Release 20220623:
* feat(./api_yamdb/reviews/models.py): подготовлены модели Category, Comment, Genre, GenreTitle, Review, Title, User
* feat(./api_yamdb/reviews/migrations): выполнены миграции
* build: разрешены конфликты в git, результаты командной работы влиты в ветку dev/sprint-10

Release 20220620:
* docs(./README.md): настройка git, определение ролей в команде

## Развернуть локально

Склонировать проект и создать виртуальное окружение:

```bash
git clone https://github.com/avtorsky/api_yamdb.git
cd api_yamdb
python -m venv venv
source venv/bin/activate
```

Проинициализировать Docker и скачать образ проекта:

```bash
docker pull avtorsky/api_yamdb:v20220729
docker image ls -a
```

В локальной директории проекта создать файл окружения .env, в который записать переменные по шаблону:

```bash
SECRET_KEY=key
HOSTS=host1,host2,...
POSTGRES_DB=yamdb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DB_HOST=host
DB_PORT=port
DEFAULT_FROM_EMAIL=email
```

После чего проинициализировать пайплайн сборки, выполнить миграции, создать суперпользователя и собрать статику:

```bash
docker-compose up -d --build
docker-compose exec web python3 manage.py migrate
docker-compose exec web python3 manage.py createsuperuser
docker-compose exec web python3 manage.py collectstatic --no-input
```

## Документация

Доступна после сборки проекта на локальном хосте по маршруту http://127.0.0.1/redoc/

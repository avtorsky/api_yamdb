# YaMDb

[Описание](#описание) /
[История изменений](#история) /
[Развернуть локально](#развернуть) /


## Описание
Проект [YaMDb](https://github.com/avtorsky/api_yamdb) собирает отзывы пользователей на произведения. В этом репозитории бэкенд проекта (приложение reviews) и API для него (приложение api), разработанные командой авторов:

* <a href="https://github.com/oitczvovich" target="_blank">oitczvovich</a>
* <a href="https://github.com/avtorsky" target="_blank">avtorsky</a>

## История изменений
Release 20220620:
* docs(./README.md): настройка git, определение ролей в команде

## Развернуть локально

```bash
git clone https://github.com/avtorsky/api_yamdb.git
cd api_yamdb
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```


# Generated by Django 3.2.13 on 2022-06-27 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220623_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Недопустимое имя', regex='^[\\w.@+-_]+$')], verbose_name='Имя пользователя'),
        ),
    ]
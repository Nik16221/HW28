# Generated by Django 4.1.2 on 2022-10-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
                ('age', models.PositiveSmallIntegerField()),
                ('role', models.CharField(choices=[('member', 'Пользователь'), ('admin', 'Администратор'), ('moderator', 'Модератор')], default='member', max_length=10)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.RemoveField(
            model_name='users',
            name='location',
        ),
    ]

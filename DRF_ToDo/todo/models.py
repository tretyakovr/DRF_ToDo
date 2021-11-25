from django.db import models
from users.models import Users


class Projects(models.Model):
    name = models.CharField(verbose_name='Наименование проекта', max_length=100, unique=True)
    comments = models.TextField(verbose_name='Примечание', blank=True)
    name_user = models.ForeignKey(Users, on_delete=models.RESTRICT, verbose_name='Автор проекта')
    start_date = models.DateField(verbose_name='Дата начала проекта')
    end_date = models.DateField(verbose_name='Дата завершения проекта')

    class Meta:
        db_table = 'Projects'
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Roles(models.Model):
    name_role = models.CharField(verbose_name='Наименование', max_length=100, unique=True)
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'Roles'
        verbose_name = 'Роли пользователей'
        verbose_name_plural = 'Роли пользователей'


class ProjectUsers(models.Model):
    name_project = models.ForeignKey(Projects, on_delete=models.RESTRICT, verbose_name='Название проекта')
    name_user = models.ForeignKey(Users, on_delete=models.RESTRICT, verbose_name='Имя пользователя')
    name_role = models.ForeignKey(Roles, on_delete=models.RESTRICT, verbose_name='Роль пользователя')
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'ProjectUsers'
        verbose_name = 'Участники проекта'
        verbose_name_plural = 'Участники проекта'


class Todo(models.Model):
    name_project = models.ForeignKey(Projects, on_delete=models.RESTRICT, verbose_name='Название проекта')
    start_date = models.DateField(verbose_name='Дата создания задачи')
    todo_text = models.TextField(verbose_name='Содержание задачи', blank=False)
    user_name = models.ForeignKey(Users, verbose_name='Автор задачи', on_delete=models.RESTRICT)
    end_date = models.DateField(verbose_name='Дата завершения задачи')
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'Todo'
        verbose_name = 'Задачи проекта'
        verbose_name_plural = 'Задачи проекта'

# Generated by Django 4.1.6 on 2023-02-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Активна'), ('blocked', 'Заблокировано')], default='active', max_length=20, verbose_name='Статус')),
                ('name', models.CharField(max_length=25, verbose_name='Статус')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('update_at', models.DateTimeField(default=None, null=True, verbose_name='Дата обновления')),
            ],
        ),
    ]

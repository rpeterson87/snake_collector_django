# Generated by Django 4.1.1 on 2022-10-03 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_snakedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snakedata',
            old_name='snakes',
            new_name='data',
        ),
    ]

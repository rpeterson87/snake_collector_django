# Generated by Django 4.1.1 on 2022-10-04 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_snakelist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SnakeList',
            new_name='SnakeLists',
        ),
    ]

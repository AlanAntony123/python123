# Generated by Django 4.1.3 on 2022-11-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-10-11'),
            preserve_default=False,
        ),
    ]

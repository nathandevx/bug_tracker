# Generated by Django 3.2.8 on 2021-11-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='', max_length=500, verbose_name='Bio'),
        ),
    ]

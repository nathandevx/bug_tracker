# Generated by Django 3.2.8 on 2021-10-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20211023_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='ticketcomment',
            options={'verbose_name': 'Ticket comment', 'verbose_name_plural': 'Ticket comments'},
        ),
        migrations.AlterModelOptions(
            name='tracker',
            options={'verbose_name': 'Tracker', 'verbose_name_plural': 'Trackers'},
        ),
    ]

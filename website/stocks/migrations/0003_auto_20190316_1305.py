# Generated by Django 2.1.5 on 2019-03-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_clientonetoone_sgonetoone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientonetoone',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='sgonetoone',
            options={'managed': False},
        ),
    ]
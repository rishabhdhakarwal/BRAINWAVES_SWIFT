# Generated by Django 2.1.7 on 2019-03-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20190316_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.ClientOneToOne')),
                ('sg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.SgOneToOne')),
            ],
        ),
    ]
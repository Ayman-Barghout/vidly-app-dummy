# Generated by Django 2.2.2 on 2019-06-25 13:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 25, 13, 58, 46, 46553, tzinfo=utc)),
        ),
    ]
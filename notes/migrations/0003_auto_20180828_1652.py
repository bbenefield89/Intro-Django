# Generated by Django 2.1 on 2018-08-28 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180828_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 16, 52, 24, 125598, tzinfo=utc)),
        ),
    ]
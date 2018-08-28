# Generated by Django 2.1 on 2018-08-28 16:47

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20180827_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 8, 28, 16, 44, 57, 196712))),
                ('calories', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('protein', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 16, 44, 57, 195934)),
        ),
    ]
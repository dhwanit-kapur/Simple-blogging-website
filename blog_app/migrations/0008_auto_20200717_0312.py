# Generated by Django 3.0.8 on 2020-07-17 03:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20200717_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 3, 12, 25, 722336, tzinfo=utc)),
        ),
    ]

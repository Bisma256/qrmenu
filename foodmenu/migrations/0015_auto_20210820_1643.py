# Generated by Django 3.2.5 on 2021-08-20 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0014_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 20, 16, 43, 37, 664130)),
        ),
    ]

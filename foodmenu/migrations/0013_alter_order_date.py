# Generated by Django 3.2.5 on 2021-08-20 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmenu', '0012_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 20, 15, 25, 58, 120087)),
        ),
    ]

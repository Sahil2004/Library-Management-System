# Generated by Django 3.2.4 on 2021-06-17 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_man', '0007_alter_borrower_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2021, 7, 2, 10, 59, 18, 489474)),
        ),
    ]
# Generated by Django 3.2.4 on 2022-02-06 16:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_man', '0009_auto_20220202_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='contact_no',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9223372036854775807), django.core.validators.MinValueValidator(-9223372036854775807)]),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2022, 2, 21, 21, 49, 40, 923558)),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-14 03:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('book_location', models.CharField(max_length=50)),
                ('status_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adm_no', models.CharField(max_length=10)),
                ('_class', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('section', models.CharField(max_length=1)),
                ('roll_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('contact_no', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1111111111)])),
            ],
        ),
    ]
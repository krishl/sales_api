# Generated by Django 2.0 on 2017-12-11 06:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')])),
                ('description', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')])),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_initial',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')]),
        ),
    ]
# Generated by Django 2.2.10 on 2020-04-18 14:38

import apps.user.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, validators=[django.core.validators.EmailValidator(), apps.user.models.UserValidator.is_email_exist]),
        ),
    ]
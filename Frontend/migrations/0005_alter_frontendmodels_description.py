# Generated by Django 4.0.1 on 2022-01-04 16:45

import Frontend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_alter_frontendmodels_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontendmodels',
            name='Description',
            field=models.FileField(upload_to=Frontend.models.FrontendModels.ReturnType),
        ),
    ]

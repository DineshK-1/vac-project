# Generated by Django 4.0.1 on 2022-01-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backendmodel',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_frontendmodels_type_alter_frontendmodels_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontendmodels',
            name='Type',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JS', 'JS')], max_length=4),
        ),
    ]

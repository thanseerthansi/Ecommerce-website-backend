# Generated by Django 4.1.2 on 2022-10-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0013_alter_missingordermodel_city_alter_ordermodel_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0014_productmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='total_price',
            field=models.FloatField(default=0.0),
        ),
    ]
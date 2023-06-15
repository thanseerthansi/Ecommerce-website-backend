# Generated by Django 4.1.2 on 2023-03-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0027_ordermodel_color_ordermodel_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingordermodel',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='missingordermodel',
            name='delivery_charge',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='missingordermodel',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='missingordermodel',
            name='size',
            field=models.FloatField(default=0.0),
        ),
    ]
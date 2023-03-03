# Generated by Django 4.1.2 on 2023-03-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0026_rename_subtotal_price_ordermodel_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='size',
            field=models.FloatField(default=0.0),
        ),
    ]

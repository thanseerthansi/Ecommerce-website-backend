# Generated by Django 4.1.2 on 2022-10-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0021_purchasestatusmodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
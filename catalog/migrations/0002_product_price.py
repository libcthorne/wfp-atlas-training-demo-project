# Generated by Django 4.0.1 on 2022-01-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]

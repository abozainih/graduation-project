# Generated by Django 4.0.3 on 2022-03-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='price_per_gallon',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
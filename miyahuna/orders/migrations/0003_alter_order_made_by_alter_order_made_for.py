# Generated by Django 4.0.3 on 2022-03-21 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_remove_order_madeby_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='made_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='made_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_user_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]

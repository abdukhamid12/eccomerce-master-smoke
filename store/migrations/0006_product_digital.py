# Generated by Django 5.0.3 on 2024-04-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

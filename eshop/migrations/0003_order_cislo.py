# Generated by Django 5.0 on 2024-01-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_alter_product_name_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cislo',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-09-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country_code',
            field=models.CharField(choices=[('SV', 'SV'), ('GT', 'GT')], default='SV', max_length=3),
        ),
    ]

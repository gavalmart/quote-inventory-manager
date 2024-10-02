# Generated by Django 4.2.16 on 2024-09-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_nas_accessory_category_nas_model_nas_accessory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nas_model',
            name='oneGb_nic_qty',
        ),
        migrations.RemoveField(
            model_name='nas_model',
            name='ram_default',
        ),
        migrations.RemoveField(
            model_name='nas_model',
            name='ram_max',
        ),
        migrations.AddField(
            model_name='nas_model',
            name='ram_default_MB',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='nas_model',
            name='ram_max_MB',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='hdd_internal_slots',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='hdd_max_expansion_units_qty',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='hdd_max_slots',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='m2_internal_slots_qty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='pci_slots_qty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='ram_slots',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='tenGb_nic_qty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='nas_model',
            name='warranty_years',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]

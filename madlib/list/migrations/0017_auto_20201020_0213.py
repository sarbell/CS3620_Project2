# Generated by Django 2.2 on 2020-10-20 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0016_auto_20201020_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formelement',
            old_name='type1',
            new_name='type',
        ),
    ]
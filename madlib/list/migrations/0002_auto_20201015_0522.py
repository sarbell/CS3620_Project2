# Generated by Django 2.2 on 2020-10-15 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='list_name',
            new_name='list_item',
        ),
    ]

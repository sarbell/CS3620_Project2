# Generated by Django 2.2 on 2020-10-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20201016_0431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lib',
            name='word_type',
        ),
        migrations.AddField(
            model_name='lib',
            name='noun',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default='0'),
        ),
    ]

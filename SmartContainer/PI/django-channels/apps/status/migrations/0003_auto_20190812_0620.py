# Generated by Django 2.2.4 on 2019-08-12 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20190812_0616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Status',
            new_name='Stat',
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-27 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0005_auto_20190814_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='EnforceH_UP',
            new_name='EnforceH_Up',
        ),
    ]
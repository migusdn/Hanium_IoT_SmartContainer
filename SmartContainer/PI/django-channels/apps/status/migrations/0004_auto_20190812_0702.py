# Generated by Django 2.2.4 on 2019-08-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20190812_0620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Conid',
            new_name='ConId',
        ),
    ]
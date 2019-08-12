# Generated by Django 2.2.4 on 2019-08-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Device_name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Device_num',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Device_status',
        ),
        migrations.AddField(
            model_name='device',
            name='Conid',
            field=models.CharField(default='B1', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='DoHumid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='DoTemper',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='Door',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device',
            name='Humid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='SetHumid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='SetTemper',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device',
            name='Temper',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='Type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='UpHumid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='UpTemper',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
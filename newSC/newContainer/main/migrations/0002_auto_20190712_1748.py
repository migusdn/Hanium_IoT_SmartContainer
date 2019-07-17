# Generated by Django 2.2.3 on 2019-07-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='container',
            name='name',
        ),
        migrations.AddField(
            model_name='container',
            name='CheckDoor',
            field=models.CharField(default='close', max_length=100),
        ),
        migrations.AddField(
            model_name='container',
            name='CheckInOut',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='CheckInOutName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ContainerID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ContainerInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ContainerloadInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='LaidupCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='LaidupPlace',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='LaidupSubCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='LocaInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='PortEntryCount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='PortEntryDate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='PortEntryYear',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='PortID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='PortName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ShipEngName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ShipKoName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ShipTypeCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='ShipTypeName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='TemInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='WetInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='batteryInfo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='vibInfo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

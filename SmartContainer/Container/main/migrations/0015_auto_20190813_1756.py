# Generated by Django 2.2.3 on 2019-08-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_container_carryingdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='container',
            options={'ordering': ['-CarryingDate', '-Check']},
        ),
        migrations.RenameField(
            model_name='container',
            old_name='LeaveClassify',
            new_name='Check',
        ),
        migrations.RemoveField(
            model_name='container',
            name='LoadID',
        ),
        migrations.RemoveField(
            model_name='container',
            name='MBLNum',
        ),
        migrations.RemoveField(
            model_name='container',
            name='Msn',
        ),
        migrations.RemoveField(
            model_name='container',
            name='Pol',
        ),
    ]
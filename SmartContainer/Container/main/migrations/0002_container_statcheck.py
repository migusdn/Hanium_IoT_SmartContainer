# Generated by Django 2.2.3 on 2019-09-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='StatCheck',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]

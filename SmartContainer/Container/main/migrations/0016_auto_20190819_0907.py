# Generated by Django 2.2.3 on 2019-08-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190813_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='container',
            options={'ordering': ['-Check', '-CarryingDate']},
        ),
        migrations.AlterField(
            model_name='container',
            name='Check',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]

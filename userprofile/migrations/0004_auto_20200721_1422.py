# Generated by Django 2.2.13 on 2020-07-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20160728_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='lang',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
    ]

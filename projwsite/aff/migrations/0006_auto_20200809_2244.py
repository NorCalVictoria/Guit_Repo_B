# Generated by Django 3.0.5 on 2020-08-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aff', '0005_auto_20200809_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='subscriber', max_length=100),
        ),
    ]

# Generated by Django 3.0.5 on 2020-08-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aff', '0003_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='user_firstd', max_length=100),
        ),
    ]
# Generated by Django 3.0.4 on 2020-07-10 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200317_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
    ]
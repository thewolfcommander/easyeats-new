# Generated by Django 3.0.4 on 2020-03-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(help_text="User's unique user id, keep it irrelated with respect to your name or email.", max_length=24, null=True, unique=True, verbose_name='username'),
        ),
    ]

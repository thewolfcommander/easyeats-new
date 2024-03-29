# Generated by Django 3.0.4 on 2020-03-15 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('message', models.TextField(null=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ReportIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('issue_type', models.CharField(choices=[('technical', 'Having issue in the web application?'), ('food', 'Having issue with the food?'), ('delivery', 'Having issue with the delivery?'), ('other', 'Having some other issue')], default='technical', max_length=255)),
                ('message', models.TextField(null=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Issue and Problem',
                'verbose_name_plural': 'Issues and Problems',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

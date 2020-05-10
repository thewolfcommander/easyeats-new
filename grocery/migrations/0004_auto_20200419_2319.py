# Generated by Django 3.0.4 on 2020-04-19 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_auto_20200419_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerycategory',
            name='description',
        ),
        migrations.CreateModel(
            name='GrocerySubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='grocery_category_feature_image')),
                ('name', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.GroceryCategory')),
            ],
            options={
                'verbose_name': 'Grocery Sub Category',
                'verbose_name_plural': 'Grocery Sub Categories',
                'ordering': ('-updated',),
            },
        ),
    ]
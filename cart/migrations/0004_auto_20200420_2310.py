# Generated by Django 3.0.4 on 2020-04-20 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0006_auto_20200420_0149'),
        ('products', '0005_remove_food_collection'),
        ('cart', '0003_auto_20200420_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='groceryentry',
            name='grocery',
        ),
        migrations.AlterField(
            model_name='cart',
            name='foods',
            field=models.ManyToManyField(to='products.Food'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='groceries',
            field=models.ManyToManyField(to='grocery.Grocery'),
        ),
        migrations.DeleteModel(
            name='FoodEntry',
        ),
        migrations.DeleteModel(
            name='GroceryEntry',
        ),
        migrations.AddField(
            model_name='entry',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='entry',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Food'),
        ),
    ]

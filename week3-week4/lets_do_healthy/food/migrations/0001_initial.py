# Generated by Django 3.1.2 on 2020-10-20 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50, null=True)),
                ('pic', models.CharField(max_length=300)),
                ('food_unit', models.CharField(max_length=50)),
                ('food_ex', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField(default=0)),
                ('total_fat', models.FloatField(default=0)),
                ('saturated_fat', models.FloatField(default=0)),
                ('trans_fat', models.FloatField(default=0)),
                ('cholesterol', models.FloatField(default=0)),
                ('sodium', models.FloatField(default=0)),
                ('potassium', models.FloatField(default=0)),
                ('total_carbohydrate', models.FloatField(default=0)),
                ('dietary_fiber', models.FloatField(default=0)),
                ('sugars', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('vitamin_A', models.FloatField(default=0)),
                ('vitamin_C', models.FloatField(default=0)),
                ('calcium', models.FloatField(default=0)),
                ('iron', models.FloatField(default=0)),
                ('nutritionFacts_ex', models.CharField(max_length=500)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
        ),
    ]

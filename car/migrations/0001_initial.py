# Generated by Django 3.2.7 on 2021-09-23 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='car.carmodel')),
            ],
            options={
                'db_table': 'photos',
            },
        ),
    ]

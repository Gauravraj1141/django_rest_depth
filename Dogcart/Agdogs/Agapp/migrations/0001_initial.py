# Generated by Django 4.0.5 on 2023-03-13 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogsBreed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('breed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogsbreed', to='Agapp.dogsbreed')),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-21 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTrali',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=444)),
                ('product_catagory', models.CharField(max_length=455)),
                ('product_price', models.IntegerField()),
                ('product_discount', models.DecimalField(decimal_places=2, default=4.23, max_digits=4)),
                ('product_desc', models.CharField(max_length=444)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_quantitiy', models.IntegerField(default=3)),
                ('pr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='srapp.producttrali')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-20 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(default='John Doe', max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('imageurl', models.URLField()),
                ('status', models.BooleanField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grocery', to='products.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]

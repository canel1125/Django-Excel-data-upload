# Generated by Django 4.0.1 on 2022-02-02 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=4)),
                ('twenty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('forty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fortyhc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('contract', models.ForeignKey(db_column='contract', on_delete=django.db.models.deletion.CASCADE, to='contract.contract', to_field='slug')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-19 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter category name', max_length=25)),
                ('display_name', models.CharField(help_text='Enter the category display name', max_length=25)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', help_text='Enter category status', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter product name', max_length=25)),
                ('display_name', models.CharField(help_text='Enter the product display name', max_length=25)),
                ('short_desciption', models.TextField(help_text='Enter short description(max=255)', max_length=255)),
                ('full_description', models.TextField(help_text='Enter full description(max=1000)', max_length=1000)),
                ('price', models.IntegerField(help_text='Enter product price')),
                ('stock', models.IntegerField(help_text='Enter Stock')),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', help_text='Enter product status', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter subcategory name', max_length=25)),
                ('display_name', models.CharField(help_text='Enter the subcategory display name', max_length=25)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1, verbose_name='Enter subcategory status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Categorie')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Subcategorie'),
        ),
    ]

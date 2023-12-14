# Generated by Django 4.2.4 on 2023-10-21 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Loyiha nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
            },
        ),
        migrations.CreateModel(
            name='ProjectName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='img/')),
                ('body', models.TextField(verbose_name='Loyiha haqida')),
                ('facebook', models.CharField(max_length=100, verbose_name='Facebook lichkasi')),
                ('whatsapp', models.CharField(max_length=100, verbose_name='Whatsapp lichkasi')),
                ('instagram', models.CharField(max_length=100, verbose_name='Instagram lichkasi')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Loyiha',
            },
        ),
    ]

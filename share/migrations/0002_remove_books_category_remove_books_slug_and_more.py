# Generated by Django 5.1.6 on 2025-03-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='category',
        ),
        migrations.RemoveField(
            model_name='books',
            name='slug',
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

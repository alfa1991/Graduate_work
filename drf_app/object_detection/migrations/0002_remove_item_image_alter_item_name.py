# Generated by Django 5.0.4 on 2024-10-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]

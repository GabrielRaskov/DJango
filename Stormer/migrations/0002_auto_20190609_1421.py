# Generated by Django 2.2.1 on 2019-06-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stormer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sauceprotecc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post_location',
        ),
        migrations.AlterField(
            model_name='image',
            name='file_name',
            field=models.CharField(max_length=20),
        ),
    ]
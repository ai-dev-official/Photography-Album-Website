# Generated by Django 3.2.8 on 2021-11-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
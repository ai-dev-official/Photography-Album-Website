# Generated by Django 3.2.9 on 2021-11-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20211112_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
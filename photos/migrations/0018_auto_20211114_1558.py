# Generated by Django 3.2.8 on 2021-11-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0017_rename_comment_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.TextField(default=False),
        ),
    ]

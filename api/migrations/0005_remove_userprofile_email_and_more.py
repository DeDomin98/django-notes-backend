# Generated by Django 4.1 on 2023-07-22 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_user_userprofile_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-05 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='Created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='Created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='last_modified',
            new_name='Last_modified',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Tittle',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='User',
        ),
    ]
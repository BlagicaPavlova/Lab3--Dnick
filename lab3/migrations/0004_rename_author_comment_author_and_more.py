# Generated by Django 4.2.2 on 2023-06-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0003_rename_tittle_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Last_modified',
            new_name='last_modified',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='User',
            new_name='user',
        ),
    ]

# Generated by Django 4.1 on 2022-08-24 18:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_kanal_playlist_video_remove_post_profil_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Account',
        ),
    ]

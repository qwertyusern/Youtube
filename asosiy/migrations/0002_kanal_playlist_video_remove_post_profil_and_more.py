# Generated by Django 4.1 on 2022-08-24 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_kanal', to='userapp.account')),
                ('connection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connect_kanal', to='userapp.connection')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_playlist', to='userapp.account')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_video', to='userapp.account')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='profil',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='profil',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='efir',
            old_name='profil',
            new_name='account',
        ),
        migrations.AlterUniqueTogether(
            name='comment_like',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='comment_like',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_account', to='userapp.account'),
        ),
        migrations.AddField(
            model_name='like',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_like', to='userapp.account'),
        ),
        migrations.AlterField(
            model_name='comment_like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to='asosiy.comment'),
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.AddField(
            model_name='video',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_video', to='asosiy.comment'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_playlist', to='asosiy.video'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_playlist', to='asosiy.video'),
        ),
        migrations.AddField(
            model_name='kanal',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_kanal', to='asosiy.video'),
        ),
        migrations.RemoveField(
            model_name='comment_like',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='profil',
        ),
        migrations.AddField(
            model_name='like',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_like', to='asosiy.video'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

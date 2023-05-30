# Generated by Django 4.2.1 on 2023-05-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_userprofile_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='profile_pic/profilepics/cat.jpg', upload_to='coverpic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/profilepics/default.jpg', upload_to='profile_pic'),
        ),
    ]

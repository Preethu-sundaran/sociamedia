# Generated by Django 4.2.1 on 2023-05-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile_cover_pic_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile_pics/dp1.jpg', null=True, upload_to='profile_pics'),
        ),
    ]

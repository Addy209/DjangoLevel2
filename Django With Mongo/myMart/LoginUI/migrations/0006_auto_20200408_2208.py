# Generated by Django 2.2.11 on 2020-04-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUI', '0005_auto_20200330_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]

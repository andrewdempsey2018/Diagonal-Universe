# Generated by Django 3.0.4 on 2020-05-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='github',
            field=models.CharField(default='No repo for this post', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube',
            field=models.CharField(default='No video for this post', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='middlePicphoto',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='post',
            name='topPicphoto',
            field=models.ImageField(upload_to='images'),
        ),
    ]

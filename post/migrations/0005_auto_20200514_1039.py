# Generated by Django 3.0.4 on 2020-05-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200512_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage1',
            field=models.CharField(default='No image', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage1Description',
            field=models.CharField(default='Description of picture', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage2',
            field=models.CharField(default='No image', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage2Description',
            field=models.CharField(default='Description of picture', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage3',
            field=models.CharField(default='No image', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='extraImage3Description',
            field=models.CharField(default='Description of picture', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='text1',
            field=models.TextField(default='No text', max_length=3000),
        ),
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default='No text', max_length=3000),
        ),
        migrations.AlterField(
            model_name='post',
            name='middlePicphotoDescription',
            field=models.CharField(default='Description of picture', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='topPicphotoDescription',
            field=models.CharField(default='Description of picture', max_length=100),
        ),
    ]
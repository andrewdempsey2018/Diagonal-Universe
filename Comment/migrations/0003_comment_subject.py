# Generated by Django 3.0.4 on 2020-07-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0002_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.SlugField(default='None', max_length=100),
        ),
    ]
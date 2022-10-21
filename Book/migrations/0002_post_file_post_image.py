# Generated by Django 4.0.3 on 2022-03-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='File',
            field=models.FileField(default='default.pdf', upload_to='media/files'),
        ),
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='media/images'),
        ),
    ]

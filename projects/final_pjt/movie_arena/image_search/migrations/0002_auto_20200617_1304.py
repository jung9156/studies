# Generated by Django 3.0.7 on 2020-06-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='img_search',
        ),
    ]

# Generated by Django 2.1.15 on 2020-06-16 17:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='img_search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('imgs', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ManyToManyField(related_name='img_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

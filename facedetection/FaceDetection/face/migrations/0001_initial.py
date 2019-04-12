# Generated by Django 2.0 on 2019-02-28 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=None, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('about', models.CharField(default=' ', max_length=150)),
                ('city', models.CharField(default='', max_length=64)),
                ('contact', models.IntegerField(default=0)),
                ('head_snap', models.ImageField(blank=True, upload_to='profile_images')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
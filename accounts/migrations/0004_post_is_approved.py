# Generated by Django 4.0.1 on 2022-12-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_pic_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
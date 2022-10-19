# Generated by Django 4.1.1 on 2022-10-17 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_about_user_about_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='id',
        ),
        migrations.AddField(
            model_name='about',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

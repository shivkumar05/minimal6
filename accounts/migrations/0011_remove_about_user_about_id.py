# Generated by Django 4.1.1 on 2022-10-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_about_id_about_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='user',
        ),
        migrations.AddField(
            model_name='about',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-08 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageblog',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='imageblog',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

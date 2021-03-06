# Generated by Django 2.2.7 on 2019-12-14 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favourite_jobs',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_favourite', through='jobs.Favourites', to='jobs.Job'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_favourite', to='jobs.Job'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='favourite_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='job_favourite', through='jobs.Favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_uuid',
            field=models.UUIDField(default=uuid.UUID('bc707068-756f-46cf-baa9-7dff216cc7b7'), editable=False),
        ),
    ]

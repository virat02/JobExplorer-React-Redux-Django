# Generated by Django 2.2.7 on 2019-12-06 03:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='JOB_ID')),
                ('job_uuid', models.UUIDField(default=uuid.UUID('655a38e2-8e77-47a9-89c1-b55225d6ef23'), editable=False)),
                ('type', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('how_to_apply', models.TextField()),
                ('language', models.CharField(max_length=200)),
                ('sponsorship_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='COMPANY_ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=200)),
                ('logo', models.ImageField(default='../companyLogo/default.png', upload_to='../companyLogo/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobs.Job')),
            ],
        ),
    ]

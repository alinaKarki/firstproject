# Generated by Django 5.0.1 on 2024-01-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_address_student_job_student_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='desc',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

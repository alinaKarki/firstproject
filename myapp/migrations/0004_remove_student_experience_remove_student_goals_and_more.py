# Generated by Django 5.0.1 on 2024-01-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_student_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='student',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='student',
            name='how_i_learn',
        ),
        migrations.RemoveField(
            model_name='student',
            name='job',
        ),
        migrations.RemoveField(
            model_name='student',
            name='job_description',
        ),
        migrations.RemoveField(
            model_name='student',
            name='what_i_know',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]

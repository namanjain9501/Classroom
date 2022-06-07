# Generated by Django 4.0.4 on 2022-04-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0020_alter_assignment_deadline_alter_assignment_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time_submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-13 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_remove_student_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]

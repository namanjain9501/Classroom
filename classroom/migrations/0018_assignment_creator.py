# Generated by Django 4.0.4 on 2022-04-26 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0017_remove_assignment_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
